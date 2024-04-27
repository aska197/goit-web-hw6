-- Find the average grade in groups for a specific subject:
SELECT groups.group_name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
JOIN students ON grades.student_id = student_id
JOIN groups ON students.group_id = group_id
WHERE grades.subject_id = 'Text Analysis'
GROUP BY groups.group_name;