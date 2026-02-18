# 📊 People Analytics KPI Pipeline

End-to-end data pipeline for institutional People Analytics monitoring, focused on KPI construction, data cleaning,and automated data quality validation.

This project simulates a structured analytics workflow for HR and governance environments, generating monthly indicators such as absenteeism, turnover, and performance metrics.

---

## 🎯 Objective

To build a reproducible analytics pipeline that:

- Integrates multiple HR data sources
- Cleans and standardizes raw data
- Generates monthly institutional KPIs
- Applies automated Data Quality (DQ) checks
- Produces curated outputs ready for BI tools (Power BI, dashboards)

---

## 🏗 Architecture
```
data/
raw/ → Original input files
clean/ → Standardized and deduplicated data
curated/ → Final KPI dataset

src/
pipeline.py → Main ETL + KPI builder
validate/
data_quality.py → Automated DQ validatio
```

---

## 📈 Generated KPIs

The pipeline produces:

- Monthly absenteeism rate
- Monthly turnover rate
- Average performance score
- Termination counts
- Total attendance records

Final output:



