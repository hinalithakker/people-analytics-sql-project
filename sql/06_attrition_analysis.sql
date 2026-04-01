SELECT 
    COUNT(CASE WHEN employee_status LIKE '%Terminated%' THEN 1 END) * 1.0 
    / COUNT(*) AS attrition_rate
FROM employees;

SELECT 
    department_type,
    COUNT(CASE WHEN employee_status LIKE '%Terminated%' THEN 1 END) AS exited,
    COUNT(*) AS total,
    ROUND(
        COUNT(CASE WHEN employee_status LIKE '%Terminated%' THEN 1 END) * 1.0 
        / COUNT(*), 3
    ) AS attrition_rate
FROM employees
GROUP BY department_type
ORDER BY attrition_rate DESC;

SELECT 
    e.employee_status,
    ROUND(AVG(g.engagement_score), 2) AS avg_engagement
FROM employees e
JOIN engagement g
    ON e.emp_id = g.emp_id
GROUP BY e.employee_status
ORDER BY avg_engagement;

SELECT 
    e.department_type,
    ROUND(AVG(g.engagement_score), 2) AS avg_engagement,
    ROUND(
        COUNT(CASE WHEN e.employee_status LIKE '%Terminated%' THEN 1 END) * 1.0 
        / COUNT(*), 3
    ) AS attrition_rate
FROM employees e
JOIN engagement g
    ON e.emp_id = g.emp_id
GROUP BY e.department_type
ORDER BY attrition_rate DESC;