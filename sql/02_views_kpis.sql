-- Monthly KPIs (example)
-- absenteeism_rate = absent_days / total_days
-- turnover_rate = terminations / headcount

-- Attendance KPIs
SELECT
  strftime('%Y-%m', date) AS month,
  SUM(CASE WHEN status = 'ABSENT' THEN 1 ELSE 0 END) AS absent_days,
  COUNT(*) AS total_days,
  1.0 * SUM(CASE WHEN status = 'ABSENT' THEN 1 ELSE 0 END) / COUNT(*) AS absenteeism_rate
FROM fact_attendance
GROUP BY 1;

-- Performance KPI
SELECT
  strftime('%Y-%m', date) AS month,
  AVG(score) AS avg_performance
FROM fact_performance
GROUP BY 1;

-- Turnover KPI
SELECT
  strftime('%Y-%m', termination_date) AS month,
  COUNT(*) AS terminations
FROM dim_employee
WHERE termination_date IS NOT NULL
GROUP BY 1;
