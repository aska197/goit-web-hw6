import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql_1 = """
SELECT s.student_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 24
GROUP BY s.student_name
ORDER BY average_grade DESC
LIMIT 1;
"""

if __name__ == '__main__':
    print('--- Select First ---')
    print(execute_query(sql_1))