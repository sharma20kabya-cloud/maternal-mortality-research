# 🩺 Maternal Mortality Research & Data Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Topic](https://img.shields.io/badge/Topic-Maternal%20Mortality-red)

## 📌 Overview

This repository contains a comprehensive data analysis and research project on **Maternal Mortality** — one of the most critical global public health challenges. The project investigates causes, trends, geographic disparities, and socioeconomic determinants of maternal deaths using publicly available datasets from WHO, UNICEF, World Bank, and government health surveys (NFHS).

> **Maternal Mortality Ratio (MMR)** is defined as the number of maternal deaths per 100,000 live births. Despite significant global progress, approximately **287,000 women** die annually due to preventable causes related to pregnancy and childbirth (WHO, 2020).

---

## 🎯 Research Objectives

1. Analyze global and regional trends in maternal mortality (2000–2023)
2. Identify key determinants: access to skilled birth attendants, antenatal care, education, income
3. Compare MMR across Indian states using NFHS-5 data
4. Examine the relationship between MMR and healthcare infrastructure
5. Build predictive models for high-risk population identification
6. Provide evidence-based policy insights

---

## 🗂️ Repository Structure

```
maternal-mortality-research/
│
├── 📁 data/
│   ├── raw/                    # Original, unmodified datasets
│   ├── processed/              # Cleaned and transformed data
│   └── external/               # Third-party reference data
│
├── 📁 notebooks/               # Jupyter notebooks for exploration & analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_EDA_global_trends.ipynb
│   ├── 04_india_state_analysis.ipynb
│   ├── 05_determinants_analysis.ipynb
│   └── 06_predictive_modeling.ipynb
│
├── 📁 src/
│   ├── analysis/               # Core analysis scripts
│   │   ├── mmr_trends.py
│   │   ├── determinants.py
│   │   └── statistical_tests.py
│   ├── visualization/          # Plotting and dashboard scripts
│   │   ├── choropleth_maps.py
│   │   ├── trend_plots.py
│   │   └── correlation_heatmaps.py
│   └── utils/                  # Helper functions
│       ├── data_loader.py
│       ├── preprocessing.py
│       └── config.py
│
├── 📁 docs/                    # Research documentation
│   ├── literature_review.md
│   ├── methodology.md
│   ├── data_dictionary.md
│   └── references.md
│
├── 📁 results/
│   ├── figures/                # Generated charts and maps
│   ├── tables/                 # Summary statistics tables
│   └── reports/                # Final research reports
│
├── 📁 tests/                   # Unit tests
│   └── test_preprocessing.py
│
├── requirements.txt
├── environment.yml
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📊 Datasets Used

| Dataset | Source | Description | Years |
|---|---|---|---|
| WHO Global MMR | World Health Organization | Global maternal mortality estimates | 2000–2020 |
| NFHS-5 | Ministry of Health, India | National Family Health Survey | 2019–2021 |
| World Bank Health Indicators | World Bank Open Data | GDP, healthcare expenditure, SBA coverage | 2000–2022 |
| UNICEF State of the World's Children | UNICEF | Child & maternal health metrics | 2010–2023 |
| SRS Statistical Report | Registrar General of India | State-wise MMR in India | 2018–2020 |

---

## 🔬 Key Research Questions

- Which states in India have the highest MMR, and what factors explain this?
- Is there a significant correlation between female literacy rate and MMR?
- How does access to skilled birth attendants (SBA) impact maternal deaths?
- What is the effect of poverty and rural-urban divide on MMR?
- Can we predict high-risk districts using socioeconomic indicators?

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Statistical visualization |
| Plotly / Folium | Interactive maps & charts |
| Scikit-learn | Predictive modeling |
| Statsmodels | Regression & statistical tests |
| Jupyter Notebook | Exploratory analysis |
| Geopandas | Geospatial analysis |

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/sharma20kabya-cloud/maternal-mortality-research.git
cd maternal-mortality-research
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebooks
```bash
jupyter notebook notebooks/
```

---

## 📈 Key Findings (Preliminary)

- 📍 **Assam, Uttar Pradesh, and Madhya Pradesh** consistently report the highest MMR in India
- 📉 India's national MMR declined from **254 (2004–06)** to **97 (2018–20)**, a 62% reduction
- 🏥 States with >80% institutional deliveries show **3x lower MMR** than states below 50%
- 📚 A 10% increase in female literacy correlates with a **~15 point reduction** in MMR
- 🌍 Sub-Saharan Africa accounts for **~70%** of global maternal deaths

---

## 📚 Literature & Theoretical Background

Key references informing this research:
- WHO (2019). *Trends in Maternal Mortality: 2000 to 2017*
- Say et al. (2014). Global causes of maternal death — The Lancet
- Registrar General of India (2022). *Special Bulletin on Maternal Mortality*
- NFHS-5 Report (2021). Ministry of Health & Family Welfare, India
- Alkema et al. (2016). Global, regional, and national levels of MMR — The Lancet

See [`docs/references.md`](docs/references.md) for the full reference list.

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add: your feature description'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

.

---

## 👩‍🔬 Author

**[Kabya Sharma]**
📧 kabyasharma69@gmail.com
🔗 [LinkedIn](www.linkedin.com/in/kabya-sharma)
---

> *"Every maternal death is a tragedy — and most are preventable."* — WHO
