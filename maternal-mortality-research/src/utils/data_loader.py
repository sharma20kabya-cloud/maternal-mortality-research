# src/utils/data_loader.py
# ============================================================
# Data Loading Utilities — Maternal Mortality Research
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path
from src.utils.config import (
    WHO_MMR_FILE, NFHS5_FILE, WORLDBANK_FILE, INDIA_SRS_FILE
)


def load_who_mmr(filepath=None) -> pd.DataFrame:
    """
    Load WHO Global Maternal Mortality dataset.

    Expected columns:
        country, iso_code, year, mmr, mmr_lower, mmr_upper,
        maternal_deaths, live_births, region

    Source: https://www.who.int/data/gho/data/themes/maternal-and-reproductive-health
    """
    path = filepath or WHO_MMR_FILE
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["mmr"]  = pd.to_numeric(df["mmr"],  errors="coerce")
    print(f"[load_who_mmr] Loaded {len(df)} rows from {path.name}")
    return df


def load_nfhs5(filepath=None) -> pd.DataFrame:
    """
    Load NFHS-5 (2019-21) state-level health indicators.

    Key columns:
        state, mmr, anc4_visits_pct, institutional_delivery_pct,
        sba_pct, female_literacy_pct, total_fertility_rate
    """
    path = filepath or NFHS5_FILE
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print(f"[load_nfhs5] Loaded {len(df)} rows from {path.name}")
    return df


def load_worldbank(filepath=None) -> pd.DataFrame:
    """
    Load World Bank health & development indicators.

    Key columns:
        country, year, gdp_per_capita, health_expenditure_pct_gdp,
        female_literacy, mmr, births_attended_by_skilled_staff
    """
    path = filepath or WORLDBANK_FILE
    df = pd.read_csv(path, skiprows=4)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print(f"[load_worldbank] Loaded {len(df)} rows from {path.name}")
    return df


def load_india_srs(filepath=None) -> pd.DataFrame:
    """
    Load India SRS (Sample Registration System) state-wise MMR data.

    Source: Registrar General of India — Special Bulletin on Maternal Mortality
    """
    path = filepath or INDIA_SRS_FILE
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print(f"[load_india_srs] Loaded {len(df)} rows from {path.name}")
    return df


def create_sample_india_mmr() -> pd.DataFrame:
    """
    Create a sample India state-wise MMR dataset for demonstration.
    Based on SRS Bulletin 2018-2020 and NFHS-5 data.
    """
    data = {
        "state": [
            "Assam", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan",
            "Odisha", "Chhattisgarh", "Bihar", "Uttarakhand",
            "Jharkhand", "Haryana", "Punjab", "Gujarat",
            "West Bengal", "Andhra Pradesh", "Telangana",
            "Tamil Nadu", "Maharashtra", "Karnataka", "Kerala"
        ],
        "mmr_2018_20": [
            195, 167, 163, 141, 136, 132, 130, 101,
            98,  96,  82,  75,  103, 58,  54,
            36,  33,  69,  19
        ],
        "institutional_delivery_pct": [
            84.6, 82.7, 80.8, 84.3, 85.8, 70.7, 76.6, 72.5,
            74.8, 92.0, 94.9, 95.4, 94.9, 97.4, 99.0,
            99.3, 95.9, 94.8, 99.8
        ],
        "anc4_visits_pct": [
            35.2, 31.0, 37.1, 28.3, 43.8, 44.9, 20.2, 56.9,
            45.0, 70.3, 71.7, 69.3, 78.6, 77.0, 79.9,
            87.2, 74.3, 81.7, 96.5
        ],
        "female_literacy_pct": [
            73.2, 59.3, 60.0, 52.1, 70.9, 60.2, 53.3, 70.7,
            56.0, 75.4, 81.4, 70.7, 71.2, 68.6, 72.3,
            82.2, 79.3, 73.1, 96.1
        ],
        "region": [
            "EAG", "EAG", "EAG", "EAG",
            "EAG", "EAG", "EAG", "Other",
            "EAG", "Other", "Other", "Other",
            "Other", "South", "South",
            "South", "Other", "South", "South"
        ]
    }
    df = pd.DataFrame(data)
    df["mmr_category"] = pd.cut(
        df["mmr_2018_20"],
        bins=[0, 70, 150, 300],
        labels=["Low", "Medium", "High"]
    )
    return df


def create_sample_global_mmr() -> pd.DataFrame:
    """
    Create a sample global MMR trend dataset for demonstration.
    Based on WHO estimates.
    """
    years = list(range(2000, 2021))
    data = {
        "year": years,
        "global_mmr":       [342, 332, 323, 313, 303, 293, 283, 273, 263, 253,
                             243, 235, 225, 215, 205, 200, 196, 193, 190, 188, 223],
        "south_asia_mmr":   [400, 383, 366, 350, 333, 317, 302, 288, 274, 261,
                             249, 237, 225, 215, 204, 194, 184, 176, 168, 160, 152],
        "sub_saharan_mmr":  [870, 852, 835, 818, 801, 785, 769, 753, 737, 721,
                             706, 691, 676, 661, 647, 633, 619, 606, 593, 580, 545],
        "india_mmr":        [370, 350, 330, 310, 290, 270, 250, 230, 210, 195,
                             180, 167, 155, 142, 130, 122, 113, 106, 103, 100,  97],
        "global_target":    [70] * len(years),   # SDG Target
    }
    return pd.DataFrame(data)
