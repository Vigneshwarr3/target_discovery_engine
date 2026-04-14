#!/usr/bin/env python3
"""
Examples: Using the CKD Target Discovery Pipeline Orchestrator

This script demonstrates various ways to use the refactored pipeline:
  1. Run the complete end-to-end pipeline
  2. Use individual stages separately
  3. Query results from DuckDB
  4. Extend the pipeline with custom analysis
"""

import logging
from pathlib import Path

from pipeline_orchestrator import (
    PipelineOrchestrator,
    GwasIngestionStage,
    LocusIdentificationStage,
    TargetPrioritizationStage,
    TargetPersistenceStage,
    StructuralHandoffStage,
)

# Configure logging for examples
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# EXAMPLE 1: Run Complete Pipeline (Simplest Approach)
# ============================================================================

def example_1_complete_pipeline():
    """Run the entire pipeline from GWAS to ColabFold in one call."""
    
    logger.info("\n" + "=" * 80)
    logger.info("EXAMPLE 1: Complete End-to-End Pipeline")
    logger.info("=" * 80)
    
    orchestrator = PipelineOrchestrator()
    
    # This single call handles all 5 stages
    results = orchestrator.run_full_pipeline(
        gwas_file=Path("metal_eGFR_meta1.TBL.map.annot.gc.gz"),
        db_path=Path("kidney_targets.duckdb"),
        output_dir=Path("colabfold_jobs"),
    )
    
    logger.info(f"\n✓ Pipeline completed!")
    logger.info(f"  Targets discovered: {results['total_targets']}")
    logger.info(f"  Database created: {results['database']}")
    logger.info(f"  Output files: {results['outputs']}")


# ============================================================================
# EXAMPLE 2: Use Individual Stages (Modular Approach)
# ============================================================================

def example_2_individual_stages():
    """Use pipeline stages separately for more control."""
    
    logger.info("\n" + "=" * 80)
    logger.info("EXAMPLE 2: Individual Pipeline Stages")
    logger.info("=" * 80)
    
    gwas_file = Path("metal_eGFR_meta1.TBL.map.annot.gc.gz")
    
    if not gwas_file.exists():
        logger.warning(f"GWAS file not found: {gwas_file}")
        return
    
    # Stage 1: Load and filter GWAS data
    logger.info("\n[Step 1] Loading GWAS data...")
    gwas_stage = GwasIngestionStage(gwas_file)
    df_filtered = gwas_stage.execute()
    logger.info(f"  Loaded {len(df_filtered)} significant variants")
    
    # Stage 2: Identify loci
    logger.info("\n[Step 2] Identifying loci via LD clumping...")
    locus_stage = LocusIdentificationStage(df_filtered)
    df_loci = locus_stage.execute()
    logger.info(f"  Found {df_loci['locus_id'].max()} loci")
    
    # Stage 3: Prioritize targets
    logger.info("\n[Step 3] Selecting lead SNPs...")
    prioritization = TargetPrioritizationStage(df_loci)
    lead_snps = prioritization.execute()
    
    # Inspect top targets
    logger.info("\n  Top 5 lead SNPs by significance:")
    for i, snp in enumerate(sorted(lead_snps, key=lambda x: x.p_value)[:5], 1):
        logger.info(
            f"    [{i}] {snp.snp_id} on chr{snp.chromosome}:{snp.position} "
            f"(p={snp.p_value:.2e}, β={snp.beta:.4f})"
        )
    
    # Stage 4: Persist targets
    logger.info("\n[Step 4] Persisting targets to DuckDB...")
    persistence = TargetPersistenceStage(lead_snps)
    db_path = persistence.execute(Path("kidney_targets.duckdb"))
    logger.info(f"  Database created: {db_path}")
    
    # Stage 5: Structural handoff
    logger.info("\n[Step 5] Preparing for ColabFold...")
    handoff = StructuralHandoffStage(lead_snps, db_path)
    outputs = handoff.execute(Path("colabfold_jobs"))
    logger.info(f"  Generated {len(outputs)} output files")


# ============================================================================
# EXAMPLE 3: Query Results from DuckDB
# ============================================================================

def example_3_query_results():
    """Query and analyze results stored in DuckDB."""
    
    logger.info("\n" + "=" * 80)
    logger.info("EXAMPLE 3: Querying Results from DuckDB")
    logger.info("=" * 80)
    
    import duckdb
    
    db_path = Path("kidney_targets.duckdb")
    
    if not db_path.exists():
        logger.warning(f"Database not found: {db_path}")
        logger.info("Run example_1 first to create the database")
        return
    
    conn = duckdb.connect(str(db_path))
    
    # Query 1: Top 10 most significant SNPs
    logger.info("\n[Query 1] Top 10 most significant SNPs:")
    top_snps = conn.execute(
        "SELECT snp_id, chromosome, position, p_value, beta, risk_direction "
        "FROM kidney_targets ORDER BY p_value LIMIT 10"
    ).df()
    
    for idx, row in top_snps.iterrows():
        logger.info(
            f"  {idx+1:2d}. {row['snp_id']:<15} "
            f"chr{row['chromosome']}:{row['position']:<12} "
            f"p={row['p_value']:.2e}  β={row['beta']:.4f}  {row['risk_direction']}"
        )
    
    # Query 2: Chromosome distribution
    logger.info("\n[Query 2] Targets per chromosome:")
    chr_dist = conn.execute(
        "SELECT chromosome, COUNT(*) as count "
        "FROM kidney_targets GROUP BY chromosome ORDER BY chromosome"
    ).df()
    
    for idx, row in chr_dist.iterrows():
        logger.info(f"  Chromosome {row['chromosome']:>2s}: {row['count']:3d} targets")
    
    # Query 3: Risk vs Protective variants
    logger.info("\n[Query 3] Effect direction:")
    effects = conn.execute(
        "SELECT risk_direction, COUNT(*) as count FROM kidney_targets "
        "GROUP BY risk_direction"
    ).df()
    
    for idx, row in effects.iterrows():
        logger.info(f"  {row['risk_direction']:<12s}: {row['count']:3d} variants")
    
    conn.close()


# ============================================================================
# EXAMPLE 4: Custom Analysis Pipeline Extension
# ============================================================================

def example_4_custom_analysis():
    """Extend the pipeline with custom analysis."""
    
    logger.info("\n" + "=" * 80)
    logger.info("EXAMPLE 4: Custom Analysis Extension")
    logger.info("=" * 80)
    
    import duckdb
    
    db_path = Path("kidney_targets.duckdb")
    
    if not db_path.exists():
        logger.warning(f"Database not found: {db_path}")
        return
    
    conn = duckdb.connect(str(db_path))
    
    # Custom analysis: Find high-confidence targets for experimental validation
    # Criteria: p < 1e-10 (ultra-significant) AND |β| > 0.005 (substantial effect)
    
    logger.info("\n[Analysis] High-confidence targets for experimental validation:")
    
    high_conf = conn.execute(
        """
        SELECT snp_id, chromosome, position, p_value, beta, risk_direction, locus_id
        FROM kidney_targets
        WHERE p_value < 1e-10 AND ABS(beta) > 0.005
        ORDER BY p_value
        """
    ).df()
    
    logger.info(f"\nFound {len(high_conf)} high-confidence targets:\n")
    
    for idx, row in high_conf.iterrows():
        logger.info(
            f"  Target {idx+1:2d}: {row['snp_id']:<15} "
            f"| p={row['p_value']:.2e} | β={row['beta']:+.4f} | "
            f"{row['risk_direction']:<12} | {row['locus_id']}"
        )
    
    # Summary statistics
    logger.info(f"\n[Summary Statistics]")
    summary = conn.execute(
        """
        SELECT 
            COUNT(*) as total_targets,
            COUNT(DISTINCT chromosome) as chromosomes,
            MIN(p_value) as best_p_value,
            AVG(beta) as mean_effect_size,
            SUM(CASE WHEN beta > 0 THEN 1 ELSE 0 END) as risk_alleles,
            SUM(CASE WHEN beta < 0 THEN 1 ELSE 0 END) as protective_alleles
        FROM kidney_targets
        """
    ).df()
    
    row = summary.iloc[0]
    logger.info(f"  Total targets:        {row['total_targets']}")
    logger.info(f"  Chromosomes covered:  {row['chromosomes']}")
    logger.info(f"  Best p-value:         {row['best_p_value']:.2e}")
    logger.info(f"  Mean effect size:     {row['mean_effect_size']:.4f}")
    logger.info(f"  Risk alleles:         {row['risk_alleles']}")
    logger.info(f"  Protective alleles:   {row['protective_alleles']}")
    
    conn.close()


# ============================================================================
# EXAMPLE 5: Batch Processing Multiple GWAS Files
# ============================================================================

def example_5_batch_processing():
    """Process multiple GWAS files in sequence."""
    
    logger.info("\n" + "=" * 80)
    logger.info("EXAMPLE 5: Batch Processing Multiple GWAS Files")
    logger.info("=" * 80)
    
    # Example: Process different phenotypes
    phenotypes = {
        "eGFR": Path("metal_eGFR_meta1.TBL.map.annot.gc.gz"),
        "CKD": Path("metal_CKD_meta1.TBL.map.annot.gc.gz"),
        "UACR": Path("metal_UACR_meta1.TBL.map.annot.gc.gz"),
    }
    
    results_summary = []
    
    for phenotype, gwas_file in phenotypes.items():
        logger.info(f"\nProcessing {phenotype}...")
        
        if not gwas_file.exists():
            logger.warning(f"  File not found: {gwas_file} (skipping)")
            continue
        
        try:
            orchestrator = PipelineOrchestrator()
            results = orchestrator.run_full_pipeline(
                gwas_file=gwas_file,
                db_path=Path(f"kidney_{phenotype.lower()}.duckdb"),
                output_dir=Path(f"colabfold_{phenotype.lower()}"),
            )
            
            results_summary.append({
                "phenotype": phenotype,
                "targets": results['total_targets'],
                "database": results['database'],
            })
            
        except Exception as e:
            logger.error(f"  Failed to process {phenotype}: {e}")
    
    logger.info("\n[Batch Processing Complete]")
    logger.info("\nSummary:")
    for summary in results_summary:
        logger.info(
            f"  {summary['phenotype']:<10} → {summary['targets']:3d} targets "
            f"saved to {summary['database']}"
        )


# ============================================================================
# MAIN: RUN SELECTED EXAMPLES
# ============================================================================

if __name__ == "__main__":
    logger.info("\n" + "=" * 80)
    logger.info("CKD TARGET DISCOVERY PIPELINE - EXAMPLES")
    logger.info("=" * 80)
    
    # Run examples (uncomment to execute)
    
    # Example 1: Complete pipeline (RECOMMENDED - run this first)
    example_1_complete_pipeline()
    
    # Example 2: Individual stages
    # example_2_individual_stages()
    
    # Example 3: Query results
    example_3_query_results()
    
    # Example 4: Custom analysis
    example_4_custom_analysis()
    
    # Example 5: Batch processing (uncomment if you have multiple GWAS files)
    # example_5_batch_processing()
    
    logger.info("\n" + "=" * 80)
    logger.info("Examples completed!")
    logger.info("=" * 80)
