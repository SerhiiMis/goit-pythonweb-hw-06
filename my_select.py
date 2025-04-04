from sqlalchemy import func, desc, Numeric
from db import Session
from models import Student, Grade, Subject, Teacher, Group

session = Session()

# 1. Топ-5 студентів з найвищим середнім балом
def select_1():
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).join(Grade).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()

# 2. Студент з найвищим середнім балом з певного предмета
def select_2(subject_id=1):
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc("avg_grade")).limit(1).first()

# 3. Середній бал у групах з певного предмета
def select_3(subject_id=1):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).select_from(Group).join(Group.students).join(Student.grades).filter(
        Grade.subject_id == subject_id
    ).group_by(Group.id).all()

# 4. Середній бал на потоці
def select_4():
    return session.query(func.round(func.avg(Grade.grade).cast(Numeric), 2)).scalar()

# 5. Курси, які читає певний викладач
def select_5(teacher_id=1):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

# 6. Список студентів у певній групі
def select_6(group_id=1):
    return session.query(Student.name).filter(Student.group_id == group_id).all()

# 7. Оцінки студентів у групі з певного предмета
def select_7(group_id=1, subject_id=1):
    return session.query(
        Student.name,
        Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

# 8. Середній бал, який ставить певний викладач
def select_8(teacher_id=1):
    return session.query(
        func.round(func.avg(Grade.grade).cast(Numeric), 2)
    ).select_from(Subject).join(Grade).filter(Subject.teacher_id == teacher_id).scalar()


# 9. Курси, які відвідує певний студент
def select_9(student_id=1):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).distinct().all()

# 10. Курси, які певному студенту читає певний викладач
def select_10(student_id=1, teacher_id=1):
    return session.query(
        Subject.name
    ).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).distinct().all()
