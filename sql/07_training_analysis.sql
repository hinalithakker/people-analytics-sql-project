SELECT 
    COUNT(t.emp_id) AS training_count,
    ROUND(AVG(e.current_employee_rating), 2) AS avg_performance
FROM employees e
LEFT JOIN training t
    ON e.emp_id = t.emp_id;


SELECT 
    e.department_type,
    COUNT(t.emp_id) AS training_sessions,
    COUNT(DISTINCT e.emp_id) AS employees,
    ROUND(COUNT(t.emp_id) * 1.0 / COUNT(DISTINCT e.emp_id), 2) AS avg_training_per_employee
FROM employees e
LEFT JOIN training t
    ON e.emp_id = t.emp_id
GROUP BY e.department_type
ORDER BY avg_training_per_employee DESC;