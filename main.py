import argparse
from db import Session
from models import Teacher, Group, Student, Subject

from my_select import (
    select_1, select_2, select_3, select_4, select_5,
    select_6, select_7, select_8, select_9, select_10,
    select_extra_1, select_extra_2
)

print("1. Топ-5 студентів з найвищим середнім балом:")
for row in select_1():
    print(row)

print("\n2. Студент з найвищим середнім балом з предмета id=1:")
print(select_2(subject_id=1))

print("\n3. Середній бал у групах з предмета id=1:")
for row in select_3(subject_id=1):
    print(row)

print("\n4. Середній бал на потоці:")
print(select_4())

print("\n5. Курси, які читає викладач id=1:")
for row in select_5(teacher_id=1):
    print(row)

print("\n6. Студенти у групі id=1:")
for row in select_6(group_id=1):
    print(row)

print("\n7. Оцінки студентів у групі id=1 з предмета id=1:")
for row in select_7(group_id=1, subject_id=1):
    print(row)

print("\n8. Середній бал, який ставив викладач id=1:")
print(select_8(teacher_id=1))

print("\n9. Курси, які відвідує студент id=1:")
for row in select_9(student_id=1):
    print(row)

print("\n10. Курси, які читає викладач id=1 студенту id=1:")
for row in select_10(student_id=1, teacher_id=1):
    print(row)

print("\nEXTRA 1. Середній бал, який викладач id=1 ставить студенту id=1:")
print(select_extra_1(student_id=1, teacher_id=1))

print("\nEXTRA 2. Оцінки студентів групи id=1 з предмета id=1 на останньому занятті:")
for row in select_extra_2(group_id=1, subject_id=1):
    print(row)



session = Session()

parser = argparse.ArgumentParser(description="CLI for database models")

parser.add_argument("-a", "--action", required=True, help="Action to perform: create, list, update, remove")
parser.add_argument("-m", "--model", required=True, help="Model: Teacher, Group, Student, Subject")

parser.add_argument("--id", type=int, help="ID of the object (for update/remove)")
parser.add_argument("-n", "--name", help="Name (for create/update)")
parser.add_argument("--group_id", type=int, help="Group ID (for Student)")
parser.add_argument("--teacher_id", type=int, help="Teacher ID (for Subject)")

args = parser.parse_args()

def get_model(name):
    return {
        "Teacher": Teacher,
        "Group": Group,
        "Student": Student,
        "Subject": Subject
    }.get(name)


def create():
    model = get_model(args.model)
    if not model:
        print("Unknown model")
        return

    if model == Teacher:
        obj = Teacher(name=args.name)
    elif model == Group:
        obj = Group(name=args.name)
    elif model == Student:
        obj = Student(name=args.name, group_id=args.group_id)
    elif model == Subject:
        obj = Subject(name=args.name, teacher_id=args.teacher_id)
    else:
        return

    session.add(obj)
    session.commit()
    print(f"{args.model} created with ID {obj.id}")


def list_all():
    model = get_model(args.model)
    if not model:
        print("Unknown model")
        return

    for obj in session.query(model).all():
        print(vars(obj))


def update():
    model = get_model(args.model)
    obj = session.get(model, args.id)
    if not obj:
        print(f"{args.model} with ID {args.id} not found")
        return

    if args.name:
        obj.name = args.name
    if args.group_id and isinstance(obj, Student):
        obj.group_id = args.group_id
    if args.teacher_id and isinstance(obj, Subject):
        obj.teacher_id = args.teacher_id

    session.commit()
    print(f"{args.model} with ID {args.id} updated")


def remove():
    model = get_model(args.model)
    obj = session.get(model, args.id)
    if not obj:
        print(f"{args.model} with ID {args.id} not found")
        return

    session.delete(obj)
    session.commit()
    print(f"{args.model} with ID {args.id} removed")

if args.action == "create":
    create()
elif args.action == "list":
    list_all()
elif args.action == "update":
    update()
elif args.action == "remove":
    remove()
else:
    print("Unknown action")
