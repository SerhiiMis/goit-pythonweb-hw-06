from my_select import (
    select_1, select_2, select_3, select_4, select_5,
    select_6, select_7, select_8, select_9, select_10
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
