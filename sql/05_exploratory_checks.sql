SELECT COUNT(DISTINCT emp_id) AS unique_employees
FROM employees;

SELECT COUNT(DISTINCT emp_id) AS unique_engagement_employees
FROM engagement;

SELECT COUNT(DISTINCT emp_id) AS unique_training_employees
FROM training;

SELECT COUNT(DISTINCT e.emp_id) AS matched_employee_engagement
FROM employees e
JOIN engagement g
    ON e.emp_id = g.emp_id;


SELECT COUNT(DISTINCT e.emp_id) AS matched_employee_training
FROM employees e
JOIN training t
    ON e.emp_id = t.emp_id;

SELECT 
    employee_status,
    COUNT(*) AS employee_count
FROM employees
GROUP BY employee_status
ORDER BY employee_count DESC;

SELECT 
    department_type,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department_type
ORDER BY employee_count DESC;

SELECT 
    AVG(engagement_score) AS avg_engagement_score,
    AVG(satisfaction_score) AS avg_satisfaction_score,
    AVG(work_life_balance_score) AS avg_work_life_balance_score
FROM engagement;

SELECT 
    e.department_type,
    ROUND(AVG(g.engagement_score), 2) AS avg_engagement_score,
    ROUND(AVG(g.satisfaction_score), 2) AS avg_satisfaction_score,
    ROUND(AVG(g.work_life_balance_score), 2) AS avg_work_life_balance_score
FROM employees e
JOIN engagement g
    ON e.emp_id = g.emp_id
GROUP BY e.department_type
ORDER BY avg_engagement_score DESC;