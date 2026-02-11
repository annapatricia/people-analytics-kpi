-- Star Schema (people analytics)

-- Dimensions
CREATE TABLE IF NOT EXISTS dim_employee (
  employee_id INTEGER PRIMARY KEY,
  name TEXT,
  department TEXT,
  role TEXT,
  hire_date DATE,
  termination_date DATE,
  location TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
  date DATE PRIMARY KEY,
  year INTEGER,
  month INTEGER,
  month_key TEXT
);

-- Facts
CREATE TABLE IF NOT EXISTS fact_attendance (
  employee_id INTEGER,
  date DATE,
  status TEXT,
  PRIMARY KEY (employee_id, date)
);

CREATE TABLE IF NOT EXISTS fact_performance (
  employee_id INTEGER,
  date DATE,
  score REAL,
  PRIMARY KEY (employee_id, date)
);
