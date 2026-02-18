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
data/curated/kpi_monthly.csv


Columns:

- month
- absent_days
- total_days
- absenteeism_rate
- avg_performance
- terminations
- turnover_rate

---

## 🧪 Data Quality Checks

Automated validation ensures:

- Unique primary keys (employee_id)
- Referential integrity (attendance ↔ employees)
- Performance score within expected range [0–5]
- Presence of required KPI columns


Columns:

- month
- absent_days
- total_days
- absenteeism_rate
- avg_performance
- terminations
- turnover_rate

---

## 🧪 Data Quality Checks

Automated validation ensures:

- Unique primary keys (employee_id)
- Referential integrity (attendance ↔ employees)
- Performance score within expected range [0–5]
- Presence of required KPI columns


Columns:

- month
- absent_days
- total_days
- absenteeism_rate
- avg_performance
- terminations
- turnover_rate

---

## 🧪 Data Quality Checks

Automated validation ensures:

- Unique primary keys (employee_id)
- Referential integrity (attendance ↔ employees)
- Performance score within expected range [0–5]
- Presence of required KPI columns

src/validate/data_quality.py

he pipeline executes DQ automatically after KPI generation.

---

## ▶️ How to Run

Install dependencies:

pip install -r requirements.txt


Run the pipeline:

python src/pipeline.py


If all validations pass, the console will display:

DQ OK
OK - generated: data/curated/kpi_monthly.csv


---

## 🧠 Technical Highlights

- Structured ETL workflow (raw → clean → curated)
- Automated Data Quality validation
- KPI aggregation via Pandas
- Modular architecture
- CI-ready structure (GitHub Actions)
- BI-ready dataset export

---

## 🏢 Application Context

Designed for:

- Institutional governance monitoring
- HR analytics environments
- Compliance & audit frameworks
- BI system integration
- Organizational performance tracking

---

## 🔮 Possible Extensions

- Integration with Power BI dashboards
- Time-series anomaly detection
- Predictive turnover modeling
- Cloud storage integration (AWS S3)
- Database-backed ingestion layer

---

## 🛠 Tech Stack

- Python
- Pandas
- JSON ingestion
- Data validation logic
- Modular ETL design












