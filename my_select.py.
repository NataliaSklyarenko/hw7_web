from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy import create_engine

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    students_with_avg_grades = session.query(Student, func.avg(Grade.grade).label('average_grade'))\
        .join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return students_with_avg_grades

def select_2(subject_id):
    student_with_highest_grade = session.query(Student, func.avg(Grade.grade).label('average_grade'))\
        .join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc()).first()
    return student_with_highest_grade

def select_3(subject_id):
    group_avg_grade = session.query(Group, func.avg(Grade.grade).label('average_grade'))\
        .join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    return group_avg_grade

def select_4():
    overall_avg_grade = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return overall_avg_grade

def select_5(teacher_id):
    courses_taught = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    return courses_taught

def select_6(group_id):
    students_in_group = session.query(Student).filter(Student.group_id == group_id).all()
    return students_in_group

def select_7(group_id, subject_id):
    grades_in_group_for_subject = session.query(Student, Grade.grade)\
        .join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    return grades_in_group_for_subject

def select_8(teacher_id):
    teacher_avg_grades = session.query(func.avg(Grade.grade).label('average_grade'))\
        .join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
    return teacher_avg_grades

def select_9(student_id):
    courses_attended = session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).all()
    return courses_attended

def select_10(student_id, teacher_id):
    courses_taught_to_student = session.query(Subject.name)\
        .join(Grade).filter(Subject.teacher_id == teacher_id, Grade.student_id == student_id).all()
    return courses_taught_to_student

# Закриваємо сесію після виконання всіх запитів
session.close()
