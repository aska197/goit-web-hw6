-- Find the grades of students in a specific group for a particular subject:
SELECT students.student_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subject_id
WHERE students.group_id = 12
AND subjects.subject_name = 'Intermediate Data Science';