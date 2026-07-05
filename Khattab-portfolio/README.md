# Khattab Salim — Data Analytics Portfolio

Three end-to-end analytics projects demonstrating SQL, Python, and BI/visualization
skills across operations, retail, and customer-retention use cases.

| # | Project | Skills | Tools |
|---|---------|--------|-------|
| 1 | **Call Center Performance & CSAT Analysis** | KPI reporting, operational analytics, root-cause analysis | Python (pandas), SQL, data visualization |
| 2 | **Retail Sales & Profitability Analysis** | Sales analytics, margin/discount analysis, BI dashboards | SQL (window functions), Python, Power BI–style reporting |
| 3 | **Customer Churn Analysis & Prediction** | Segmentation, predictive modeling, driver analysis | Python (pandas, scikit-learn), logistic regression |

## Repository structure
```
portfolio/
├── data/      # datasets (CSV)
├── code/      # Python analysis scripts
├── sql/       # SQL query sets
├── charts/    # generated visualizations
└── README.md
```

## Project summaries

### 1. Call Center Performance & CSAT Analysis
Analyzed 4,000 support tickets to explain what drives customer satisfaction.
**Key finding:** CSAT drops sharply once handle time exceeds channel norms, and a
9-point FCR gap between teams explained most of the CSAT variance — pointing to
coaching, not staffing, as the highest-ROI fix.

### 2. Retail Sales & Profitability Analysis
Analyzed ~10.6M AED of sales across regions, segments, and categories using SQL and Python.
**Key finding:** Technology orders turn unprofitable above a ~20% discount, while
Office Supplies stay healthy — a case for category-specific discount caps.

### 3. Customer Churn Analysis & Prediction
Built a logistic-regression model (ROC-AUC 0.82) to identify at-risk customers.
**Key finding:** Month-to-month contracts, low tenure, and frequent support calls are
the strongest churn drivers — a targeted retention offer to this segment is the clear play.

## Notes
Datasets are realistic simulations generated for demonstration; all analysis code,
SQL, and visualizations are fully reproducible from the scripts in this repository.
