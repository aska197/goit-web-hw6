-- List of courses taught by a specific teacher to a specific student:
SELECT DISTINCT subjects.subject_name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE grades.student_id = 'Steven Costa'
AND teachers.teacher_name = 'Professor Mcdonald';