# ColabFold Input Cell (paste into ColabFold Colab notebook)
# This cell prepares kidney disease variant structures for folding.

import json

# Kidney disease targets from GWAS pipeline
KIDNEY_TARGETS = [{"id": "UNK_rs2433601", "gene": "Phe809Leu"}, {"id": "UNK_rs77924615", "gene": "Ile445Val"}, {"id": "UNK_rs28817415", "gene": "Phe485Leu"}, {"id": "UNK_rs10224210", "gene": "Phe65Leu"}, {"id": "UNK_rs10866705", "gene": "Ile711Leu"}, {"id": "UNK_rs1047891", "gene": "Ile503Leu"}, {"id": "UNK_rs9895661", "gene": "Phe864Leu"}, {"id": "UNK_rs35969577", "gene": "Phe795Val"}, {"id": "UNK_rs963837", "gene": "Phe697Leu"}, {"id": "UNK_rs62435145", "gene": "Phe856Val"}]

# Job submission
queries = []
for target in KIDNEY_TARGETS:
    protein_id = target["id"]
    gene_name = target["gene"]
    query = f">{gene_name}|{protein_id}\n{protein_id}"
    queries.append(query)

# Format for ColabFold MSA search
query_sequence = "\n".join(queries)

print(f"✓ Prepared {len(queries)} targets for ColabFold")
print(f"  Sample query:\n{queries[0][:80]}...")

# Paste the query_sequence into ColabFold's "sequence" input field
print(f"\nQuery length: {len(query_sequence)} characters")
print("\n→ Copy 'query_sequence' output and paste into ColabFold notebook.")
