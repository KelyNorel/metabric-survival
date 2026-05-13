"""
ingest.py — METABRIC clinical data ingestion and cleaning
"""

import pandas as pd
import numpy as np

RAW = "data/raw/brca_metabric_clinical_data.tsv"
OUT = "data/processed/clinical_clean.csv"

df = pd.read_csv(RAW, sep="\t", low_memory=False)
print(f"Raw shape: {df.shape}")

# ── Survival endpoints ─────────────────────────────────────────────────────
df["os_months"] = pd.to_numeric(df["OS_MONTHS"], errors="coerce")
df["os_event"]  = (df["OS_STATUS"].str.startswith("1")).astype(int)
df["rfs_months"] = pd.to_numeric(df["RFS_MONTHS"], errors="coerce")
df["rfs_event"]  = (df["RFS_STATUS"].str.split(":").str[1] == "Recurred").astype(int)

# ── Clinical features ──────────────────────────────────────────────────────
df["age"]       = pd.to_numeric(df["AGE_AT_DIAGNOSIS"], errors="coerce")
df["grade"]     = pd.to_numeric(df["GRADE"], errors="coerce")
df["tumor_size"] = pd.to_numeric(df["TUMOR_SIZE"], errors="coerce")
df["lymph_nodes"] = pd.to_numeric(df["LYMPH_NODES_EXAMINED_POSITIVE"], errors="coerce")
df["npi"]       = pd.to_numeric(df["NPI"], errors="coerce")
df["subtype"]   = df["CLAUDIN_SUBTYPE"].str.strip()
df["er"]        = df["ER_STATUS"].str.strip()
df["her2"]      = df["HER2_STATUS"].str.strip()
df["pr"]        = df["PR_STATUS"].str.strip()
df["chemo"]     = df["CHEMOTHERAPY"].str.strip()
df["hormone_tx"] = df["HORMONE_THERAPY"].str.strip()
df["stage"]     = pd.to_numeric(df["TUMOR_STAGE"], errors="coerce")

# ── Keep relevant columns ──────────────────────────────────────────────────
keep = ["patientId", "os_months", "os_event", "rfs_months", "rfs_event",
        "age", "grade", "tumor_size", "lymph_nodes", "npi",
        "subtype", "er", "her2", "pr", "chemo", "hormone_tx", "stage"]

clean = df[keep].dropna(subset=["os_months", "os_event"])

print(f"Clean shape: {clean.shape}")
print(f"OS event rate: {clean['os_event'].mean():.1%}")
print(f"RFS event rate: {clean['rfs_event'].mean():.1%}")
print(f"Median follow-up: {clean['os_months'].median():.1f} months")
print(f"\nSubtype counts:\n{clean['subtype'].value_counts(dropna=False)}")

clean.to_csv(OUT, index=False)
print(f"\n✓ Saved to {OUT}")