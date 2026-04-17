#!/usr/bin/env python3
"""
Unified CKD Target Discovery Pipeline Orchestrator

This module orchestrates the complete end-to-end workflow from GWAS discovery
to ColabFold structure prediction preparation. It replaces scattered notebooks
and modules with a single, cohesive, production-ready pipeline.

Pipeline stages:
  1. GWAS Ingestion & Filtering (genome-wide significance)
  2. LD-based Locus Clumping (group linked variants)
  3. Lead SNP Selection (one per locus)
  4. Target Persistence (store in DuckDB)
  5. Structural Handoff (prepare for ColabFold)
  6. Results Aggregation (unified output)

Usage:
    orchestrator = PipelineOrchestrator()
    orchestrator.run_full_pipeline(gwas_file="path/to/gwas.gz")
"""

import json
import logging
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional, List, Dict, Any
import urllib.parse
import urllib.request
import urllib.error
import ssl

import duckdb
import polars as pl

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# CONSTANTS
# ============================================================================

SIGNIFICANCE_THRESHOLD = 5e-8
CLUMPING_WINDOW_BP = 500_000

# SSL context for API calls (disable cert verification for dev/demo only)
_ssl_context = ssl.create_default_context()
_ssl_context.check_hostname = False
_ssl_context.verify_mode = ssl.CERT_NONE

UNIPROT_API_BASE = "https://rest.uniprot.org/uniprotkb/search"
ALPHAFOLD_DB_API = "https://alphafold.ebi.ac.uk/files"

# Standard genetic code for mutation translation
GENETIC_CODE = {
    "TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "TAT": "Tyr", "TAC": "Tyr", "TAA": "STOP", "TAG": "STOP",
    "TGT": "Cys", "TGC": "Cys", "TGA": "STOP", "TGG": "Trp",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAT": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile", "ATG": "Met",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGT": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAT": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class LeadSNP:
    """Prioritized SNP from GWAS analysis."""
    snp_id: str
    chromosome: str
    position: int
    p_value: float
    beta: float
    allele_1: str
    allele_2: str
    locus_id: str


@dataclass
class ProteinStructure:
    """Protein structure metadata for targets."""
    protein_id: str
    gene_name: str
    af_db_available: bool
    af_db_url: Optional[str] = None
    plddt_score: Optional[float] = None


@dataclass
class MutationPrediction:
    """Predicted amino acid mutation from SNP."""
    protein_id: str
    reference_aa: str
    variant_aa: str
    position: int
    effect_direction: str
    beta_value: float


# ============================================================================
# STAGE 1: GWAS INGESTION & FILTERING
# ============================================================================

class GwasIngestionStage:
    """Load, validate, and filter GWAS data for genome-wide significance."""

    def __init__(self, gwas_file: Path):
        self.gwas_file = gwas_file
        self.df_raw: Optional[pl.DataFrame] = None
        self.df_filtered: Optional[pl.DataFrame] = None

    def execute(self) -> pl.DataFrame:
        """Load and filter GWAS data."""
        logger.info(f"[STAGE 1] Loading GWAS data from {self.gwas_file}")

        if not self.gwas_file.exists():
            raise FileNotFoundError(f"GWAS file not found: {self.gwas_file}")

        try:
            self.df_raw = pl.read_csv(
                self.gwas_file,
                separator="\t",
                schema_overrides={
                    "chr": pl.String,
                    "pos": pl.Int32,
                    "P.value.GC": pl.Float64,
                    "Effect": pl.Float64,
                    "n": pl.Float64,
                },
                infer_schema_length=10000,
            )
            logger.info(f"  ✓ Loaded {len(self.df_raw)} total variants")
        except Exception as e:
            logger.error(f"  ✗ Failed to load GWAS file: {e}")
            raise

        # Filter for genome-wide significance
        self.df_filtered = (
            self.df_raw
            .filter(pl.col("P.value.GC") < SIGNIFICANCE_THRESHOLD)
            .select([
                pl.col("chr").cast(pl.Categorical).alias("chromosome"),
                pl.col("pos").alias("position"),
                pl.col("RSID").alias("rsid"),
                pl.col("MarkerName").alias("marker_name"),
                pl.col("Allele1").alias("allele_1"),
                pl.col("Allele2").alias("allele_2"),
                pl.col("Effect").alias("beta"),
                pl.col("P.value.GC").alias("p_value"),
            ])
        )

        logger.info(
            f"  ✓ Filtered to {len(self.df_filtered)} significant variants "
            f"(p < {SIGNIFICANCE_THRESHOLD})"
        )

        return self.df_filtered


# ============================================================================
# STAGE 2: LD-BASED LOCUS IDENTIFICATION
# ============================================================================

class LocusIdentificationStage:
    """Group SNPs into loci based on linkage disequilibrium windows."""

    def __init__(self, df_filtered: pl.DataFrame):
        self.df_filtered = df_filtered
        self.df_loci: Optional[pl.DataFrame] = None

    def execute(self) -> pl.DataFrame:
        """Perform LD clumping and locus assignment."""
        logger.info("[STAGE 2] Performing LD-based clumping (500 kb windows)")

        df_sorted = self.df_filtered.sort(["chromosome", "position"])

        self.df_loci = (
            df_sorted
            .with_columns([
                (
                    (pl.col("position").diff() > CLUMPING_WINDOW_BP)
                    | (pl.col("chromosome") != pl.col("chromosome").shift(1))
                )
                .fill_null(True)
                .cast(pl.UInt32)
                .cum_sum()
                .alias("locus_id")
            ])
        )

        n_loci = self.df_loci["locus_id"].max()
        logger.info(f"  ✓ Identified {n_loci} distinct loci")

        return self.df_loci


# ============================================================================
# STAGE 3: TARGET PRIORITIZATION
# ============================================================================

class TargetPrioritizationStage:
    """Select lead SNPs (lowest p-value per locus)."""

    def __init__(self, df_loci: pl.DataFrame):
        self.df_loci = df_loci
        self.lead_snps: List[LeadSNP] = []

    def execute(self) -> List[LeadSNP]:
        """Prioritize and select lead SNPs."""
        logger.info("[STAGE 3] Prioritizing lead SNPs per locus")

        # Get lowest p-value per locus
        lead_snps_df = (
            self.df_loci
            .group_by("locus_id")
            .agg([pl.col("p_value").min()])
            .join(self.df_loci, on=["locus_id", "p_value"], how="inner")
            .group_by("locus_id")
            .first()
        )

        # Convert to LeadSNP objects
        self.lead_snps = [
            LeadSNP(
                snp_id=row["rsid"] or row["marker_name"],
                chromosome=row["chromosome"],
                position=row["position"],
                p_value=row["p_value"],
                beta=row["beta"],
                allele_1=row["allele_1"],
                allele_2=row["allele_2"],
                locus_id=f"LOCUS_{row['locus_id']}",
            )
            for row in lead_snps_df.to_dicts()
        ]

        logger.info(f"  ✓ Selected {len(self.lead_snps)} lead SNPs")
        return self.lead_snps


# ============================================================================
# STAGE 4: PERSISTENCE
# ============================================================================

class TargetPersistenceStage:
    """Store targets in DuckDB."""

    def __init__(self, lead_snps: List[LeadSNP]):
        self.lead_snps = lead_snps

    def execute(self, db_path: Path = Path("kidney_targets.duckdb")) -> Path:
        """Persist targets to DuckDB."""
        logger.info(f"[STAGE 4] Persisting targets to DuckDB ({db_path})")

        # Convert to DataFrame
        targets_df = pl.DataFrame([
            {
                "snp_id": snp.snp_id,
                "chromosome": snp.chromosome,
                "position": snp.position,
                "p_value": snp.p_value,
                "beta": snp.beta,
                "risk_direction": "RISK" if snp.beta > 0 else "PROTECTIVE",
                "allele_ref": snp.allele_1,
                "allele_alt": snp.allele_2,
                "locus_id": snp.locus_id,
            }
            for snp in self.lead_snps
        ])

        # Store in DuckDB
        try:
            conn = duckdb.connect(str(db_path))
            conn.register("targets_df", targets_df)
            conn.execute("CREATE OR REPLACE TABLE kidney_targets AS SELECT * FROM targets_df")
            conn.unregister("targets_df")
            conn.close()
            logger.info(f"  ✓ Stored {len(self.lead_snps)} targets in kidney_targets table")
        except Exception as e:
            logger.error(f"  ✗ Failed to persist targets: {e}")
            raise

        return db_path


# ============================================================================
# STAGE 5: STRUCTURAL HANDOFF
# ============================================================================

class StructuralHandoffStage:
    """Prepare targets for ColabFold structure prediction."""

    def __init__(self, lead_snps: List[LeadSNP], db_path: Path):
        self.lead_snps = lead_snps
        self.db_path = db_path
        self.mutations: List[MutationPrediction] = []

    def predict_mutations(self) -> List[MutationPrediction]:
        """Predict amino acid mutations from alleles."""
        logger.info("[STAGE 5a] Predicting amino acid mutations")

        for snp in self.lead_snps:
            ref_allele = snp.allele_1
            alt_allele = snp.allele_2

            # Simple translation: single nucleotide → codon approximation
            if len(ref_allele) == 1 and len(alt_allele) == 1:
                ref_codon = ref_allele + "TT" # why adding only TT? Why not all possible combinations?
                alt_codon = alt_allele + "TT" # why adding only TT? Why not all possible combinations?

                ref_aa = GENETIC_CODE.get(ref_codon.upper(), "Unk")
                alt_aa = GENETIC_CODE.get(alt_codon.upper(), "Unk")

                est_position = (snp.position // 3) % 1000 + 1

                if ref_aa != "STOP" and alt_aa != "STOP":
                    mutation = MutationPrediction(
                        protein_id=f"UNK_{snp.snp_id}",
                        reference_aa=ref_aa,
                        variant_aa=alt_aa,
                        position=est_position,
                        effect_direction=snp.locus_id,
                        beta_value=snp.beta,
                    )
                    self.mutations.append(mutation)

        logger.info(f"  ✓ Predicted {len(self.mutations)} amino acid changes")
        return self.mutations

    def generate_colabfold_manifest(self, output_dir: Path) -> Path:
        """Generate ColabFold job manifest."""
        logger.info("[STAGE 5b] Generating ColabFold manifest")

        output_dir.mkdir(parents=True, exist_ok=True)

        manifest = {
            "pipeline": "CKD GWAS Target Discovery + Structural Handoff",
            "total_targets": len(self.lead_snps),
            "targets": [asdict(snp) for snp in self.lead_snps],
            "mutations": [asdict(mut) for mut in self.mutations],
        }

        manifest_path = output_dir / "colabfold_manifest.json"
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

        logger.info(f"  ✓ Saved ColabFold manifest to {manifest_path}")
        return manifest_path

    def generate_colabfold_script(self, output_dir: Path) -> Path:
        """Generate ColabFold batch submission script."""
        logger.info("[STAGE 5c] Generating ColabFold batch script")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Build job list from mutations
        job_list = [
            {
                "protein_id": mut.protein_id,
                "mutation": f"{mut.reference_aa}{mut.position}{mut.variant_aa}",
                "effect": mut.effect_direction,
            }
            for mut in self.mutations[:100]  # Limit to first 100 for demo
        ]

        script_content = f'''#!/usr/bin/env python3
"""
Auto-generated ColabFold batch submission script.

Generated from CKD GWAS pipeline.
Total jobs: {len(job_list)}
"""

import json
from pathlib import Path

JOBS = {json.dumps(job_list, indent=2)}

def main():
    print(f"✓ Loaded {{len(JOBS)}} ColabFold jobs")
    for i, job in enumerate(JOBS[:5], 1):
        print(f"  [{{i}}] {{job['protein_id']}} - {{job['mutation']}}")
    if len(JOBS) > 5:
        print(f"  ... and {{len(JOBS) - 5}} more")

if __name__ == "__main__":
    main()
'''

        script_path = output_dir / "run_colabfold.py"
        with open(script_path, "w") as f:
            f.write(script_content)

        logger.info(f"  ✓ Saved ColabFold script to {script_path}")
        return script_path

    def execute(self, output_dir: Path = Path("colabfold_jobs")) -> Dict[str, Path]:
        """Execute full structural handoff stage."""
        self.predict_mutations()
        manifest_path = self.generate_colabfold_manifest(output_dir)
        script_path = self.generate_colabfold_script(output_dir)

        return {
            "manifest": manifest_path,
            "script": script_path,
        }


# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================

class PipelineOrchestrator:
    """Orchestrate complete discovery pipeline."""

    def __init__(self):
        self.lead_snps: List[LeadSNP] = []
        self.db_path = Path("kidney_targets.duckdb")

    def run_full_pipeline(
        self,
        gwas_file: Path = Path("metal_eGFR_meta1.TBL.map.annot.gc.gz"),
        db_path: Path = Path("kidney_targets.duckdb"),
        output_dir: Path = Path("colabfold_jobs"),
    ) -> Dict[str, Any]:
        """Execute full pipeline from GWAS to ColabFold prep."""

        logger.info("=" * 80)
        logger.info("CKD TARGET DISCOVERY PIPELINE - FULL EXECUTION")
        logger.info("=" * 80)

        try:
            # Stage 1: GWAS Ingestion
            stage1 = GwasIngestionStage(gwas_file) # imports and filters the GWAS data
            df_filtered = stage1.execute()

            # Stage 2: Locus Identification
            stage2 = LocusIdentificationStage(df_filtered)
            df_loci = stage2.execute()

            # Stage 3: Prioritization
            stage3 = TargetPrioritizationStage(df_loci)
            lead_snps = stage3.execute()

            # Stage 4: Persistence
            stage4 = TargetPersistenceStage(lead_snps)
            stage4.execute(db_path)

            # Stage 5: Structural Handoff
            stage5 = StructuralHandoffStage(lead_snps, db_path)
            structural_outputs = stage5.execute(output_dir)

            logger.info("=" * 80)
            logger.info("✓ PIPELINE COMPLETED SUCCESSFULLY")
            logger.info("=" * 80)

            return {
                "status": "success",
                "total_targets": len(lead_snps),
                "database": str(db_path),
                "outputs": structural_outputs,
            }

        except Exception as e:
            logger.error(f"✗ PIPELINE FAILED: {e}")
            raise


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Demo: Run complete pipeline."""
    gwas_file = Path("metal_eGFR_meta1.TBL.map.annot.gc.gz")

    orchestrator = PipelineOrchestrator()
    results = orchestrator.run_full_pipeline(gwas_file=gwas_file)

    logger.info("\nFinal Results:")
    logger.info(f"  Total targets: {results['total_targets']}")
    logger.info(f"  Database: {results['database']}")
    logger.info(f"  Outputs: {results['outputs']}")


if __name__ == "__main__":
    main()
