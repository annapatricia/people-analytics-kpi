from pathlib import Path
import pandas as pd
import json

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw"
CLEAN = BASE / "data" / "clean"
CURATED = BASE / "data" / "curated"

def load_raw():
    employees = pd.read_csv(RAW / "employees.csv", parse_dates=["hire_date", "termination_date"])
    attendance = pd.read_csv(RAW / "attendance.csv", parse_dates=["date"])
    performance = pd.DataFrame(json.loads((RAW / "performance.json").read_text(encoding="utf-8")))
    performance["date"] = pd.to_datetime(performance["date"])
    return employees, attendance, performance

def clean_data(employees, attendance, performance):
    # basic standardization
    employees.columns = [c.strip().lower() for c in employees.columns]
    attendance.columns = [c.strip().lower() for c in attendance.columns]
    performance.columns = [c.strip().lower() for c in performance.columns]

    # drop duplicates
    employees = employees.drop_duplicates(subset=["employee_id"])
    attendance = attendance.drop_duplicates(subset=["employee_id", "date"])
    performance = performance.drop_duplicates(subset=["employee_id", "date"])

    CLEAN.mkdir(parents=True, exist_ok=True)
    employees.to_csv(CLEAN / "employees_clean.csv", index=False)
    attendance.to_csv(CLEAN / "attendance_clean.csv", index=False)
    performance.to_csv(CLEAN / "performance_clean.csv", index=False)
    return employees, attendance, performance

def build_kpis(employees, attendance, performance):
    # monthly absenteeism: absent days / total records (proxy for workdays in sample)
    attendance["month"] = attendance["date"].dt.to_period("M").astype(str)

    abs_month = (
        attendance.assign(is_absent=(attendance["status"] == "ABSENT").astype(int))
        .groupby(["month"])["is_absent"]
        .agg(absent_days="sum", total_days="count")
        .reset_index()
    )
    abs_month["absenteeism_rate"] = abs_month["absent_days"] / abs_month["total_days"]

    # turnover: terminations in month / headcount (simple)
    employees["term_month"] = employees["termination_date"].dt.to_period("M").astype(str)
    terminations = employees.dropna(subset=["termination_date"]).groupby("term_month")["employee_id"].nunique().reset_index()
    terminations = terminations.rename(columns={"term_month": "month", "employee_id": "terminations"})

    headcount = employees["employee_id"].nunique()
    terminations["turnover_rate"] = terminations["terminations"] / headcount

    # performance avg per month
    performance["month"] = performance["date"].dt.to_period("M").astype(str)
    perf_month = performance.groupby("month")["score"].mean().reset_index().rename(columns={"score":"avg_performance"})

    # merge kpis
    kpi = abs_month.merge(perf_month, on="month", how="left").merge(terminations, on="month", how="left")
    kpi["terminations"] = kpi["terminations"].fillna(0).astype(int)
    kpi["turnover_rate"] = kpi["turnover_rate"].fillna(0)

    CURATED.mkdir(parents=True, exist_ok=True)
    kpi.to_csv(CURATED / "kpi_monthly.csv", index=False)
    return kpi

def main():
    employees, attendance, performance = load_raw()
    employees, attendance, performance = clean_data(employees, attendance, performance)
    kpi = build_kpis(employees, attendance, performance)
    print("OK - generated:", (CURATED / "kpi_monthly.csv"))

if __name__ == "__main__":
    main()
