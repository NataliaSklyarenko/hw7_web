from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Створення об'єкта базової моделі
Base = declarative_base()

# Модель студентів
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    grades = relationship('Grade')

# Модель груп
class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student')

# Модель викладачів
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship('Subject')

# Модель предметів
class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    grades = relationship('Grade')

# Модель оцінок
class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Float)
    date_received = Column(DateTime)

# Створення об'єкта для взаємодії з базою даних
engine = create_engine('sqlite:///school.db')

# Створення таблиць у базі даних
Base.metadata.create_all(engine)
