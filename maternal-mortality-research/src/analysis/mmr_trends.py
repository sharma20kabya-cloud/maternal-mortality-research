# src/analysis/mmr_trends.py
# ============================================================
# MMR Trend Analysis — Maternal Mortality Research
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from scipy import stats
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.utils.config import FIGURES_DIR, TABLES_DIR, PLOT_STYLE
from src.utils.data_loader import create_sample_global_mmr, create_sample_india_mmr


# ── Style ────────────────────────────────────────────────────
try:
    plt.style.use(PLOT_STYLE)
except:
    plt.style.use("seaborn-v0_8-whitegrid")

COLORS = {
    "global":        "#e15759",
    "south_asia":    "#f28e2b",
    "sub_saharan":   "#76b7b2",
    "india":         "#4e79a7",
    "target":        "#59a14f",
    "high":          "#d62728",
    "medium":        "#ff7f0e",
    "low":           "#2ca02c",
}


# ══════════════════════════════════════════════════════════════
# 1. Global MMR Trend Analysis
# ══════════════════════════════════════════════════════════════

def analyze_global_trends(df: pd.DataFrame) -> dict:
    """
    Compute descriptive statistics and trend metrics for global MMR data.

    Returns a dict with summary stats and linear regression slope
    for each region.
    """
    results = {}
    regions = {
        "Global":       "global_mmr",
        "South Asia":   "south_asia_mmr",
        "Sub-Saharan":  "sub_saharan_mmr",
        "India":        "india_mmr",
    }

    for label, col in regions.items():
        series = df[col].dropna()
        slope, intercept, r, p, se = stats.linregress(df["year"], series)
        pct_change = ((series.iloc[-1] - series.iloc[0]) / series.iloc[0]) * 100
        results[label] = {
            "2000_mmr":      round(series.iloc[0], 1),
            "2020_mmr":      round(series.iloc[-1], 1),
            "pct_change":    round(pct_change, 1),
            "annual_slope":  round(slope, 2),
            "r_squared":     round(r**2, 4),
            "p_value":       round(p, 6),
        }

    return results


def plot_global_mmr_trends(df: pd.DataFrame, save: bool = True):
    """Line chart of MMR trends by region, 2000–2020."""
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df["year"], df["global_mmr"],      color=COLORS["global"],
            linewidth=2.5, marker="o", markersize=4, label="Global")
    ax.plot(df["year"], df["south_asia_mmr"],   color=COLORS["south_asia"],
            linewidth=2.5, marker="s", markersize=4, label="South Asia")
    ax.plot(df["year"], df["sub_saharan_mmr"],  color=COLORS["sub_saharan"],
            linewidth=2.5, marker="^", markersize=4, label="Sub-Saharan Africa")
    ax.plot(df["year"], df["india_mmr"],        color=COLORS["india"],
            linewidth=3.0, marker="D", markersize=5, label="India")
    ax.axhline(70, color=COLORS["target"], linewidth=1.8,
               linestyle="--", label="SDG Target (70)")

    ax.fill_between(df["year"], df["india_mmr"], 70,
                    alpha=0.08, color=COLORS["india"])

    ax.set_title("Global Maternal Mortality Ratio Trends (2000–2020)",
                 fontsize=15, fontweight="bold", pad=15)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("MMR (per 100,000 live births)", fontsize=12)
    ax.legend(fontsize=11, loc="upper right")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.set_xlim(2000, 2020)
    ax.annotate("SDG 3.1 Target", xy=(2019, 72), fontsize=9,
                color=COLORS["target"], style="italic")

    plt.tight_layout()
    if save:
        out = FIGURES_DIR / "global_mmr_trends.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print(f"[plot] Saved → {out}")
    plt.show()
    return fig


# ══════════════════════════════════════════════════════════════
# 2. India State-wise Analysis
# ══════════════════════════════════════════════════════════════

def plot_india_statewise_mmr(df: pd.DataFrame, save: bool = True):
    """Horizontal bar chart — India state-wise MMR ranked."""
    df_sorted = df.sort_values("mmr_2018_20", ascending=True)

    color_map = {"High": COLORS["high"], "Medium": COLORS["medium"],
                 "Low": COLORS["low"]}
    colors = df_sorted["mmr_category"].map(color_map)

    fig, ax = plt.subplots(figsize=(10, 9))
    bars = ax.barh(df_sorted["state"], df_sorted["mmr_2018_20"],
                   color=colors, edgecolor="white", height=0.7)

    ax.axvline(70,  color=COLORS["target"], linestyle="--",
               linewidth=1.5, label="SDG Target (70)")
    ax.axvline(167, color="#888888", linestyle=":",
               linewidth=1.2, label="National Avg (167)")

    for bar, val in zip(bars, df_sorted["mmr_2018_20"]):
        ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height()/2,
                str(val), va="center", ha="left", fontsize=9)

    # Legend patches
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COLORS["high"],   label="High MMR (>150)"),
        Patch(facecolor=COLORS["medium"], label="Medium MMR (70–150)"),
        Patch(facecolor=COLORS["low"],    label="Low MMR (<70)"),
    ]
    ax.legend(handles=legend_elements + [
        plt.Line2D([0], [0], color=COLORS["target"], linestyle="--", label="SDG Target"),
        plt.Line2D([0], [0], color="#888888", linestyle=":",  label="National Avg"),
    ], fontsize=9, loc="lower right")

    ax.set_title("India: State-wise Maternal Mortality Ratio (2018–20)",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("MMR (per 100,000 live births)", fontsize=11)
    ax.set_xlim(0, 240)

    plt.tight_layout()
    if save:
        out = FIGURES_DIR / "india_statewise_mmr.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print(f"[plot] Saved → {out}")
    plt.show()
    return fig


# ══════════════════════════════════════════════════════════════
# 3. Correlation Analysis
# ══════════════════════════════════════════════════════════════

def plot_mmr_correlations(df: pd.DataFrame, save: bool = True):
    """Scatter plots — MMR vs key determinants for Indian states."""
    determinants = {
        "institutional_delivery_pct": "Institutional Delivery (%)",
        "anc4_visits_pct":            "4+ Antenatal Care Visits (%)",
        "female_literacy_pct":        "Female Literacy Rate (%)",
    }

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Determinants of Maternal Mortality — Indian States",
                 fontsize=14, fontweight="bold", y=1.02)

    for ax, (col, label) in zip(axes, determinants.items()):
        x = df[col]
        y = df["mmr_2018_20"]
        slope, intercept, r, p, _ = stats.linregress(x, y)

        color_pts = df["mmr_category"].map({
            "High": COLORS["high"], "Medium": COLORS["medium"], "Low": COLORS["low"]
        })
        ax.scatter(x, y, c=color_pts, s=90, edgecolors="white",
                   linewidth=0.8, zorder=3)

        # Regression line
        x_line = np.linspace(x.min(), x.max(), 100)
        ax.plot(x_line, slope * x_line + intercept,
                color="#333333", linewidth=1.5, linestyle="--", alpha=0.7)

        # State labels
        for _, row in df.iterrows():
            ax.annotate(row["state"][:3], (row[col], row["mmr_2018_20"]),
                        fontsize=7, alpha=0.75,
                        xytext=(3, 3), textcoords="offset points")

        ax.set_xlabel(label, fontsize=10)
        ax.set_ylabel("MMR (per 100,000 live births)", fontsize=10)
        ax.set_title(f"r = {r:.2f}  |  p = {p:.3f}", fontsize=10)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save:
        out = FIGURES_DIR / "mmr_determinants_scatter.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print(f"[plot] Saved → {out}")
    plt.show()
    return fig


def compute_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Return Pearson correlation matrix for numeric MMR indicators."""
    numeric_cols = [
        "mmr_2018_20", "institutional_delivery_pct",
        "anc4_visits_pct", "female_literacy_pct"
    ]
    corr = df[numeric_cols].corr()
    print("\n── Correlation Matrix ──")
    print(corr.round(3))
    return corr


def plot_correlation_heatmap(df: pd.DataFrame, save: bool = True):
    """Annotated heatmap of the correlation matrix."""
    corr = compute_correlation_matrix(df)
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)

    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdYlGn_r",
                center=0, vmin=-1, vmax=1, ax=ax,
                linewidths=0.5, cbar_kws={"shrink": 0.8})
    ax.set_title("Correlation Matrix — MMR & Health Determinants",
                 fontsize=13, fontweight="bold", pad=10)

    labels = {
        "mmr_2018_20":                  "MMR",
        "institutional_delivery_pct":   "Institutional\nDelivery %",
        "anc4_visits_pct":              "ANC4\nVisits %",
        "female_literacy_pct":          "Female\nLiteracy %",
    }
    ax.set_xticklabels([labels.get(c, c) for c in corr.columns], fontsize=9)
    ax.set_yticklabels([labels.get(c, c) for c in corr.index], fontsize=9, rotation=0)

    plt.tight_layout()
    if save:
        out = FIGURES_DIR / "correlation_heatmap.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print(f"[plot] Saved → {out}")
    plt.show()
    return fig


# ══════════════════════════════════════════════════════════════
# 4. Summary Report
# ══════════════════════════════════════════════════════════════

def generate_summary_table(india_df: pd.DataFrame) -> pd.DataFrame:
    """Create a formatted summary statistics table by MMR category."""
    cols = ["mmr_2018_20", "institutional_delivery_pct",
            "anc4_visits_pct", "female_literacy_pct"]

    summary = india_df.groupby("mmr_category")[cols].agg(["mean", "min", "max"])
    summary.columns = [f"{c[0]}_{c[1]}" for c in summary.columns]
    summary = summary.round(1)

    out = TABLES_DIR / "mmr_summary_by_category.csv"
    summary.to_csv(out)
    print(f"[table] Saved → {out}")
    print("\n── Summary by MMR Category ──")
    print(summary)
    return summary


# ══════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  Maternal Mortality Research — Analysis Pipeline")
    print("=" * 60)

    # Load sample data
    global_df = create_sample_global_mmr()
    india_df  = create_sample_india_mmr()

    # Global trend analysis
    print("\n[1] Global MMR Trend Statistics")
    stats_dict = analyze_global_trends(global_df)
    for region, metrics in stats_dict.items():
        print(f"\n  {region}:")
        for k, v in metrics.items():
            print(f"    {k:<18} : {v}")

    # Plots
    print("\n[2] Generating plots...")
    plot_global_mmr_trends(global_df)
    plot_india_statewise_mmr(india_df)
    plot_mmr_correlations(india_df)
    plot_correlation_heatmap(india_df)

    # Summary table
    print("\n[3] Summary Table")
    generate_summary_table(india_df)

    print("\n✅ Analysis complete! Check results/ for outputs.")
