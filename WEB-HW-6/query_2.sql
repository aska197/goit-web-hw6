-- Find the student with the highest average grade in a specific subject:
SELECT student_id, AVG(grade) AS average_grade
FROM grades
WHERE subject_id = 'Introduction to Databases'
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 1;