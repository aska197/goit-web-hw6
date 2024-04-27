-- Find the courses taught by a specific teacher:
SELECT subj.subject_name
FROM subjects subj
JOIN teachers t ON subj.teacher_id = t.id
WHERE t.teacher_name = 'Professor Mcdonald';