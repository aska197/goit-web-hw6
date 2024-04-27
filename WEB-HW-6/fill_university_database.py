from datetime import datetime
import faker
from random import choice, randint
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 7  # 7 relevant subjects
NUMBER_TEACHERS = randint(3, 5)
MAX_GRADES_PER_STUDENT = 20

def generate_fake_data(number_students, number_groups, number_subjects, number_teachers) -> tuple:
    fake = faker.Faker()

    # Generate student names
    students = [fake.name() for _ in range(number_students)]

    # Generate group names like FL-45, FL-46, FL-47
    groups = [f"FL-{i}" for i in range(45, 45 + number_groups)]

    # Generate relevant subjects
    subjects = ["Intermediate Data Science", "English Language", "Translation Theory",
                "Introduction to Databases", "Python Development", 
                "Systems of Automated Translation", "Text Analysis"]

    # Generate teacher names with 'Professor' or 'Doctor' in them
    teachers =  [f"Professor {fake.last_name()}" for _ in range(number_teachers)]

    return students, groups, teachers, subjects

def prepare_data(students, groups, teachers, subjects) -> tuple:
    # Prepare data for students table
    students_data = [(student, choice(groups)) for student in students]

    # Prepare data for groups table
    groups_data = [(group,) for group in groups]

    # Prepare data for teachers table
    teachers_data = [(teacher,) for teacher in teachers]

    # Prepare data for subjects table
    subjects_data = [(subject, choice(teachers)) for subject in subjects]

    return students_data, groups_data, teachers_data, subjects_data

def generate_grades(students, subjects) -> list:
    fake = faker.Faker()
    grades = []
    for student in students:
        for _ in range(randint(1, MAX_GRADES_PER_STUDENT)):
            grade = fake.random_int(min=50, max=100)  # Random grade between 50 and 100
            subject = choice(subjects)
            date_received = fake.date_between(start_date='-1y', end_date='today')  # Generate a random date within the past year
            date_received_str = date_received.strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM-DD'
            grades.append((student[0], subject[0], grade, date_received_str))  # Include date_received
    return grades


def insert_data_to_db(students, groups, teachers, subjects, grades) -> None:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

        # Insert data into groups table
        cur.executemany("INSERT INTO groups (group_name) VALUES (?)", groups)

        # Insert data into students table
        cur.executemany("INSERT INTO students (student_name, group_id) VALUES (?, (SELECT id FROM groups WHERE group_name = ?))", students)

        # Insert data into teachers table
        cur.executemany("INSERT INTO teachers (teacher_name) VALUES (?)", teachers)

        # Insert data into subjects table
        cur.executemany("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, (SELECT id FROM teachers WHERE teacher_name = ?))", subjects)

        # Insert data into grades table
        cur.executemany("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)", grades)

        # Commit the changes
        con.commit()

if __name__ == "__main__":
    students, groups, teachers, subjects = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_TEACHERS)
    students_data, groups_data, teachers_data, subjects_data = prepare_data(students, groups, teachers, subjects)
    grades = generate_grades(students_data, subjects_data)  # Pass subjects_data instead of subjects
    insert_data_to_db(students_data, groups_data, teachers_data, subjects_data, grades)
