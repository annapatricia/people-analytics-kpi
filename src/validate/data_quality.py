from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
CLEAN = BASE / "data" / "clean"
CURATED = BASE / "data" / "curated"

def assert_true(cond: bool, msg: str):
    if not cond:
        raise ValueError(msg)

def run():
    emp = pd.read_csv(CLEAN / "employees_clean.csv")
    att = pd.read_csv(CLEAN / "attendance_clean.csv")
    perf = pd.read_csv(CLEAN / "performance_clean.csv")
    kpi = pd.read_csv(CURATED / "kpi_monthly.csv")

    # 1) primary key uniqueness
    assert_true(emp["employee_id"].is_unique, "employees_clean: employee_id is not unique")

    # 2) attendance employee_id exists in employees
    missing = set(att["employee_id"]) - set(emp["employee_id"])
    assert_true(len(missing) == 0, f"attendance_clean: employee_id not found in employees: {sorted(list(missing))}")

    # 3) performance score range
    assert_true(((perf["score"] >= 0) & (perf["score"] <= 5)).all(), "performance_clean: score out of [0,5]")

    # 4) KPI columns present
    expected = {"month","absent_days","total_days","absenteeism_rate","avg_performance","terminations","turnover_rate"}
    assert_true(expected.issubset(set(kpi.columns)), f"kpi_monthly missing columns: {expected - set(kpi.columns)}")

    print("DQ OK")

if __name__ == "__main__":
    run()
