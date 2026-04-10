# src/utils/config.py
# ============================================================
# Project Configuration — Maternal Mortality Research
# ============================================================

import os
from pathlib import Path

# ── Project Root ────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parents[2]

# ── Data Paths ──────────────────────────────────────────────
DATA_DIR       = ROOT_DIR / "data"
RAW_DIR        = DATA_DIR / "raw"
PROCESSED_DIR  = DATA_DIR / "processed"
EXTERNAL_DIR   = DATA_DIR / "external"

# ── Results Paths ───────────────────────────────────────────
RESULTS_DIR    = ROOT_DIR / "results"
FIGURES_DIR    = RESULTS_DIR / "figures"
TABLES_DIR     = RESULTS_DIR / "tables"
REPORTS_DIR    = RESULTS_DIR / "reports"

# ── Notebook Path ───────────────────────────────────────────
NOTEBOOKS_DIR  = ROOT_DIR / "notebooks"

# ── Create dirs if missing ──────────────────────────────────
for d in [RAW_DIR, PROCESSED_DIR, EXTERNAL_DIR,
          FIGURES_DIR, TABLES_DIR, REPORTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ── Dataset Filenames ───────────────────────────────────────
WHO_MMR_FILE         = RAW_DIR / "who_mmr_global_2000_2020.csv"
NFHS5_FILE           = RAW_DIR / "nfhs5_state_indicators.csv"
WORLDBANK_FILE       = RAW_DIR / "worldbank_health_indicators.csv"
INDIA_SRS_FILE       = RAW_DIR / "india_srs_mmr_2018_2020.csv"
INDIA_SHAPEFILE      = EXTERNAL_DIR / "india_states.shp"

# ── Analysis Parameters ─────────────────────────────────────
REFERENCE_YEAR       = 2020
MMR_HIGH_THRESHOLD   = 200    # MMR above this = high risk
MMR_LOW_THRESHOLD    = 70     # MMR below this = low risk
SIGNIFICANCE_LEVEL   = 0.05   # Alpha for statistical tests

# ── Indian States of Interest ────────────────────────────────
HIGH_BURDEN_STATES = [
    "Assam", "Uttar Pradesh", "Madhya Pradesh",
    "Rajasthan", "Odisha", "Chhattisgarh", "Bihar"
]

LOW_BURDEN_STATES = [
    "Kerala", "Maharashtra", "Tamil Nadu",
    "Telangana", "Andhra Pradesh"
]

# ── Plot Settings ────────────────────────────────────────────
PLOT_STYLE      = "seaborn-v0_8-whitegrid"
FIGURE_DPI      = 150
FIGURE_FORMAT   = "png"
COLOR_HIGH_MMR  = "#d62728"   # red
COLOR_LOW_MMR   = "#2ca02c"   # green
COLOR_INDIA     = "#1f77b4"   # blue
COLOR_GLOBAL    = "#ff7f0e"   # orange

print(f"[config] Project root: {ROOT_DIR}")
