-- Data Quality Checks (examples)

-- 1) Duplicate employees
SELECT employee_id, COUNT(*) AS n
FROM dim_employee
GROUP BY employee_id
HAVING COUNT(*) > 1;

-- 2) Attendance rows without employee
SELECT a.*
FROM fact_attendance a
LEFT JOIN dim_employee e ON e.employee_id = a.employee_id
WHERE e.employee_id IS NULL;

-- 3) Performance score range sanity
SELECT *
FROM fact_performance
WHERE score < 0 OR score > 5;
