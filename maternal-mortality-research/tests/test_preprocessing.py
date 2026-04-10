# tests/test_preprocessing.py
# ============================================================
# Unit Tests — Maternal Mortality Research
# ============================================================

import pytest
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.utils.data_loader import create_sample_india_mmr, create_sample_global_mmr


class TestIndiaMmrData:
    def setup_method(self):
        self.df = create_sample_india_mmr()

    def test_dataframe_not_empty(self):
        assert len(self.df) > 0

    def test_required_columns_exist(self):
        required = ["state", "mmr_2018_20", "institutional_delivery_pct",
                    "anc4_visits_pct", "female_literacy_pct"]
        for col in required:
            assert col in self.df.columns, f"Missing column: {col}"

    def test_mmr_values_positive(self):
        assert (self.df["mmr_2018_20"] > 0).all()

    def test_mmr_values_realistic(self):
        assert self.df["mmr_2018_20"].max() < 1000
        assert self.df["mmr_2018_20"].min() > 0

    def test_percentages_in_range(self):
        for col in ["institutional_delivery_pct", "anc4_visits_pct", "female_literacy_pct"]:
            assert self.df[col].between(0, 100).all(), f"{col} out of 0–100 range"

    def test_mmr_category_column_exists(self):
        assert "mmr_category" in self.df.columns

    def test_mmr_category_valid_values(self):
        valid = {"Low", "Medium", "High"}
        actual = set(self.df["mmr_category"].astype(str).unique()) - {"nan"}
        assert actual.issubset(valid), f"Unexpected categories: {actual - valid}"

    def test_kerala_lowest_mmr(self):
        kerala = self.df[self.df["state"] == "Kerala"]["mmr_2018_20"].values[0]
        assert kerala == self.df["mmr_2018_20"].min(), "Kerala should have lowest MMR"

    def test_no_duplicate_states(self):
        assert self.df["state"].nunique() == len(self.df)


class TestGlobalMmrData:
    def setup_method(self):
        self.df = create_sample_global_mmr()

    def test_year_range(self):
        assert self.df["year"].min() == 2000
        assert self.df["year"].max() == 2020

    def test_declining_india_mmr(self):
        india = self.df["india_mmr"]
        assert india.iloc[-1] < india.iloc[0], "India MMR should decline over time"

    def test_no_null_values(self):
        assert self.df.isnull().sum().sum() == 0

    def test_sdg_target_constant(self):
        assert (self.df["global_target"] == 70).all()
