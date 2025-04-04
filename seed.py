from faker import Faker
from random import randint, choice
from datetime import date
from db import Session
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()
session = Session()

# Create groups
groups = [Group(name=f'Group {i}') for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Create teachers
teachers = [Teacher(name=fake.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()

# Create subjects
subjects = [Subject(name=f'Subject {i}', teacher=choice(teachers)) for i in range(1, 9)]
session.add_all(subjects)
session.commit()

# Create students
students = [Student(name=fake.name(), group=choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Create grades
for student in students:
    for subject in subjects:
        for _ in range(randint(3, 5)):  # 3-5 grades per subject
            grade = Grade(
                student=student,
                subject=subject,
                grade=round(randint(60, 100) / 10, 1),
                date_of=fake.date_between(start_date='-1y', end_date='today')
            )
            session.add(grade)

session.commit()
session.close()
print("Seeding complete.")
