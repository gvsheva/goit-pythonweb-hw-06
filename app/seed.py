#!/usr/bin/env python

import random
from faker import Faker
from sqlalchemy import select, func
from app.db import SessionLocal
from app.models import Group, Teacher, Subject, Student, Grade

fake = Faker()


def run():
    session = SessionLocal()
    try:
        groups = [Group(name=f"G-{i+1}") for i in range(3)]
        session.add_all(groups)

        teachers = [Teacher(full_name=fake.name()) for _ in range(random.randint(3, 5))]
        session.add_all(teachers)

        subjects = []
        for _ in range(random.randint(5, 8)):
            subjects.append(
                Subject(
                    name=fake.unique.job()[:90],
                    teacher=random.choice(teachers),
                )
            )
        session.add_all(subjects)

        students = []
        for _ in range(random.randint(30, 50)):
            students.append(
                Student(
                    full_name=fake.name(),
                    group=random.choice(groups),
                )
            )
        session.add_all(students)
        session.commit()

        for st in students:
            for subj in subjects:
                for _ in range(random.randint(0, 20)):
                    session.add(
                        Grade(
                            student=st,
                            subject=subj,
                            value=random.randint(40, 100),
                        )
                    )
        session.commit()

        totals = {
            "groups":   session.scalar(select(func.count()).select_from(Group)),
            "teachers": session.scalar(select(func.count()).select_from(Teacher)),
            "subjects": session.scalar(select(func.count()).select_from(Subject)),
            "students": session.scalar(select(func.count()).select_from(Student)),
            "grades":   session.scalar(select(func.count()).select_from(Grade)),
        }
        print(totals)
    finally:
        session.close()


if __name__ == "__main__":
    run()
