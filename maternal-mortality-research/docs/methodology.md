# Research Methodology

## Study Design

This project employs a **quantitative cross-sectional and longitudinal** research design to analyze maternal mortality trends and determinants.

---

## Data Sources

| Source | Type | Coverage |
|--------|------|----------|
| WHO MMR Estimates | Secondary | Global, 2000–2020 |
| NFHS-5 (2019-21) | Secondary | India, state-level |
| SRS Bulletin (2018-20) | Secondary | India, state-level |
| World Bank Indicators | Secondary | Global, 2000–2022 |

---

## Analytical Approach

### 1. Descriptive Analysis
- Frequency distributions and summary statistics
- Time-series trend analysis (2000–2020)
- State-wise ranking and categorization

### 2. Correlation Analysis
- Pearson correlation between MMR and determinants
- Variables: institutional delivery %, ANC4 visits %, female literacy %, GDP per capita

### 3. Regression Analysis
- OLS regression: MMR ~ literacy + institutional delivery + ANC4 + healthcare expenditure
- Check: multicollinearity (VIF), normality of residuals, homoscedasticity

### 4. Geospatial Mapping
- Choropleth maps using Geopandas + Folium
- State-level and district-level MMR visualization

### 5. Predictive Modeling (optional)
- Random Forest / XGBoost classifier for high-risk district prediction
- Features: SBA coverage, literacy, poverty index, healthcare access

---

## Statistical Tests

| Test | Purpose |
|------|---------|
| Pearson's r | Bivariate correlation |
| OLS Regression | Multivariate determinant analysis |
| ANOVA | Compare MMR across regional groups |
| Chi-square | Association between categorical variables |

---

## Definitions

- **MMR**: Maternal deaths per 100,000 live births
- **Maternal death**: Death during pregnancy or within 42 days of delivery
- **EAG States**: Empowered Action Group states (high-burden states in India)
- **SBA**: Skilled Birth Attendant
- **ANC4**: Four or more antenatal care visits
