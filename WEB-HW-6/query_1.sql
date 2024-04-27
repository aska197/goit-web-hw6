-- Find the 5 students with the highest average grade across all subjects:
SELECT s.student_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.student_name = g.student_id
GROUP BY s.student_name
ORDER BY average_grade DESC
LIMIT 5;
