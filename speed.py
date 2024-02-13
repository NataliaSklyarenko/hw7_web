from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime, timedelta
import random

# Створення підключення до бази даних
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація Faker
fake = Faker()

# Функція для створення випадкових даних для студентів
def create_students(num_students):
    students = []
    for _ in range(num_students):
        student = Student(name=fake.name())
        students.append(student)
    return students

# Функція для створення випадкових даних для груп
def create_groups(num_groups):
    groups = []
    for _ in range(num_groups):
        group = Group(name=fake.random_element(elements=('A', 'B', 'C')))
        groups.append(group)
    return groups

# Функція для створення випадкових даних для викладачів
def create_teachers(num_teachers):
    teachers = []
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        teachers.append(teacher)
    return teachers

# Функція для створення випадкових даних для предметів
def create_subjects(num_subjects, teachers):
    subjects = []
    for _ in range(num_subjects):
        teacher = random.choice(teachers)
        subject = Subject(name=fake.random_element(elements=('Math', 'Science', 'History')),
                          teacher=teacher)
        subjects.append(subject)
    return subjects

# Функція для створення випадкових оцінок для студентів з предметів
def create_grades(students, subjects):
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(5, 20)):
                date_received = fake.date_time_between(start_date='-1y', end_date='now')
                grade = Grade(student=student, subject=subject, grade=random.uniform(2, 5),
                              date_received=date_received)
                session.add(grade)

# Створення та заповнення студентів, груп, викладачів і предметів
students = create_students(50)
groups = create_groups(3)
teachers = create_teachers(5)
subjects = create_subjects(8, teachers)

session.add_all(students)
session.add_all(groups)
session.add_all(teachers)
session.add_all(subjects)
session.commit()

# Заповнення оцінок для студентів з предметів
create_grades(students, subjects)

# Закриття сесії
session.close()
