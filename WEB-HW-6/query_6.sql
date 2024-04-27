-- Find the list of students in a specific group:
SELECT student_name
FROM students
WHERE group_id = (SELECT id FROM groups WHERE group_name = 'FL-47');