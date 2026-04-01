CREATE TABLE employees (
    emp_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    start_date TEXT,
    exit_date TEXT,
    title TEXT,
    supervisor TEXT,
    ad_email TEXT,
    business_unit TEXT,
    employee_status TEXT,
    employee_type TEXT,
    pay_zone TEXT,
    employee_classification_type TEXT,
    termination_type TEXT,
    termination_description TEXT,
    department_type TEXT,
    division TEXT,
    dob TEXT,
    state TEXT,
    job_function_description TEXT,
    gender_code TEXT,
    location_code TEXT,
    race_desc TEXT,
    marital_desc TEXT,
    performance_score TEXT,
    current_employee_rating INTEGER
);

CREATE TABLE engagement (
    emp_id INTEGER,
    survey_date TEXT,
    engagement_score INTEGER,
    satisfaction_score INTEGER,
    work_life_balance_score INTEGER
);

CREATE TABLE training (
    emp_id INTEGER,
    training_date TEXT,
    training_program_name TEXT,
    training_type TEXT,
    training_outcome TEXT,
    location TEXT,
    trainer TEXT,
    training_duration_days INTEGER,
    training_cost REAL
);