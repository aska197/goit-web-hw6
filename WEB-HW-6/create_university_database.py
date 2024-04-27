import sqlite3

def create_database():
    # читаємо файл зі скриптом для створення БД
    with open('/Users/reiraserizawa/Documents/goit-web-hw6/WEB-HW-6/university.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


if __name__ == "__main__":
    create_database()
