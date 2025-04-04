# Homework 6 — SQLAlchemy + Alembic + PostgreSQL + CLI

This project implements a student-grade database using PostgreSQL, SQLAlchemy, Alembic for migrations, and a custom CLI tool for CRUD operations.

## 📦 Stack

- Python 3.12
- PostgreSQL
- SQLAlchemy
- Alembic
- Faker
- argparse

## 📁 Project structure

```
.
├── alembic/              # Alembic migrations
├── models.py             # SQLAlchemy models
├── db.py                 # Database connection
├── init_db.py            # Create tables
├── seed.py               # Seed script (for testing)
├── my_select.py          # 10 homework queries + 2 extra queries
├── main.py               # CLI for CRUD operations
└── README.md
```

## 🧪 Example CLI commands

### 👨‍🏫 Teacher

```
py main.py -a create -m Teacher -n "Boris Johnson"
py main.py -a list -m Teacher
py main.py -a update -m Teacher --id 3 -n "Andry Bezos"
py main.py -a remove -m Teacher --id 3
```

### 🧑‍🎓 Student

```
py main.py -a create -m Student -n "Alice Adams" --group_id 1
py main.py -a list -m Student
py main.py -a update -m Student --id 5 -n "Alice Smith" --group_id 2
py main.py -a remove -m Student --id 5
```

### 👥 Group

```
py main.py -a create -m Group -n "AD-101"
py main.py -a list -m Group
```

### 📘 Subject

```
py main.py -a create -m Subject -n "Math" --teacher_id 1
py main.py -a list -m Subject
```

## 📊 Select queries

Run `main.py` without arguments to test predefined queries in `my_select.py`, including:

- Top 5 students by average grade
- Student with highest average grade in a subject
- Average grade per group for a subject
- Average grade across all students
- Courses by teacher
- Students in a group
- Grades in a group for a subject
- Teacher’s average grade across subjects
- Courses per student
- Courses a teacher teaches to a specific student

### 🧠 Extra queries:

- Average grade a teacher gave to a specific student
- Grades at the last lesson for a group and subject

## 🛠 Setup

1. Start PostgreSQL via Docker:

```
docker run --name goit-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

2. Run Alembic migrations:

```
alembic upgrade head
```

3. (Optional) Seed database:

```
python seed.py
```

## ✅ Done!

This project fully meets the base and advanced requirements of homework 6.
