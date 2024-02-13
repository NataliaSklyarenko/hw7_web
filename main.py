import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade

# Підключення до бази даних
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

# Функція для створення запису в базі даних
def create_record(model, **kwargs):
    record = model(**kwargs)
    session.add(record)
    session.commit()
    print(f"{model.__name__} створено")

# Функція для виведення списку записів з бази даних
def list_records(model):
    records = session.query(model).all()
    for record in records:
        print(record)

# Функція для оновлення запису в базі даних
def update_record(model, record_id, **kwargs):
    record = session.query(model).filter_by(id=record_id).first()
    if record:
        for attr, value in kwargs.items():
            setattr(record, attr, value)
        session.commit()
        print(f"{model.__name__} оновлено")
    else:
        print(f"{model.__name__} з id={record_id} не знайдено")

# Функція для видалення запису з бази даних
def remove_record(model, record_id):
    record = session.query(model).filter_by(id=record_id).first()
    if record:
        session.delete(record)
        session.commit()
        print(f"{model.__name__} з id={record_id} видалено")
    else:
        print(f"{model.__name__} з id={record_id} не знайдено")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI програма для CRUD операцій з базою даних")
    parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"], required=True,
                        help="Дія, яку потрібно виконати (create, list, update, remove)")
    parser.add_argument("--model", "-m", choices=["Student", "Group", "Teacher", "Subject", "Grade"], required=True,
                        help="Модель, над якою потрібно провести операцію")
    parser.add_argument("--id", type=int, help="ID запису для оновлення або видалення")
    parser.add_argument("--name", help="Ім'я запису для створення або оновлення")

    args = parser.parse_args()

    if args.action == "create":
        if args.model == "Student":
            create_record(Student, name=args.name)
        elif args.model == "Group":
            create_record(Group, name=args.name)
        elif args.model == "Teacher":
            create_record(Teacher, name=args.name)
        elif args.model == "Subject":
            create_record(Subject, name=args.name)
        elif args.model == "Grade":
            print("Оцінки створюються автоматично при додаванні студента до предмету")
    elif args.action == "list":
        if args.model == "Student":
            list_records(Student)
        elif args.model == "Group":
            list_records(Group)
        elif args.model == "Teacher":
            list_records(Teacher)
        elif args.model == "Subject":
            list_records(Subject)
        elif args.model == "Grade":
            list_records(Grade)
    elif args.action == "update":
        if args.model == "Student":
            update_record(Student, args.id, name=args.name)
        elif args.model == "Group":
            update_record(Group, args.id, name=args.name)
        elif args.model == "Teacher":
            update_record(Teacher, args.id, name=args.name)
        elif args.model == "Subject":
            update_record(Subject, args.id, name=args.name)
        elif args.model == "Grade":
            print("Оцінки не можна оновити окремо, вони залежать від студентів і предметів")
    elif args.action == "remove":
        if args.model == "Student":
            remove_record(Student, args.id)
        elif args.model == "Group":
            remove_record(Group, args.id)
        elif args.model == "Teacher":
            remove_record(Teacher, args.id)
        elif args.model == "Subject":
            remove_record(Subject, args.id)
        elif args.model == "Grade":
            print("Оцінки видаляються автоматично при видаленні студента або предмету")

    session.close()
        
