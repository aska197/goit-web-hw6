-- Find the list of courses attended by a specific student:
SELECT DISTINCT subjects.subject_name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = 'Anna Robles';
