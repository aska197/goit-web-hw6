-- Find the average grade given by a specific teacher for their subjects:
SELECT teachers.teacher_name, AVG(grades.grade) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
GROUP BY teachers.teacher_name;