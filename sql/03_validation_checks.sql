SELECT 'employees' AS table_name, COUNT(*) FROM employees
UNION ALL
SELECT 'engagement', COUNT(*) FROM engagement
UNION ALL
SELECT 'training', COUNT(*) FROM training;