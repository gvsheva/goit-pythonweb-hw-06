#!/usr/bin/env python

from sqlalchemy import select, func, desc, distinct
from app.db import SessionLocal
from app.models import Student, Group, Subject, Grade


def select_1():
    with SessionLocal() as s:
        q = (
            select(
                Student.id,
                Student.full_name,
                func.avg(Grade.value).label("avg_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
        )
        return s.execute(q).all()


def select_2(subject_id: int):
    with SessionLocal() as s:
        q = (
            select(
                Student.id,
                Student.full_name,
                func.avg(Grade.value).label("avg_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .where(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(1)
        )
        return s.execute(q).first()


def select_3(subject_id: int):
    with SessionLocal() as s:
        q = (
            select(
                Group.id,
                Group.name,
                func.avg(Grade.value).label("avg_grade"),
            )
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .where(Grade.subject_id == subject_id)
            .group_by(Group.id)
            .order_by(Group.name)
        )
        return s.execute(q).all()


def select_4():
    with SessionLocal() as s:
        q = select(func.avg(Grade.value).label("avg_grade"))
        return s.execute(q).scalar_one()


def select_5(teacher_id: int):
    with SessionLocal() as s:
        q = select(Subject.id, Subject.name).where(Subject.teacher_id == teacher_id)
        return s.execute(q).all()


def select_6(group_id: int):
    with SessionLocal() as s:
        q = (
            select(Student.id, Student.full_name)
            .where(Student.group_id == group_id)
            .order_by(Student.full_name)
        )
        return s.execute(q).all()


def select_7(group_id: int, subject_id: int):
    with SessionLocal() as s:
        q = (
            select(
                Student.full_name,
                Grade.value,
                Grade.created_at,
            )
            .join(Grade, Grade.student_id == Student.id)
            .where(Student.group_id == group_id, Grade.subject_id == subject_id)
            .order_by(Student.full_name, Grade.created_at)
        )
        return s.execute(q).all()


def select_8(teacher_id: int):
    with SessionLocal() as s:
        q = (
            select(func.avg(Grade.value))
            .join(Subject, Subject.id == Grade.subject_id)
            .where(Subject.teacher_id == teacher_id)
        )
        return s.execute(q).scalar_one()


def select_9(student_id: int):
    with SessionLocal() as s:
        q = (
            select(distinct(Subject.id), Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .where(Grade.student_id == student_id)
            .order_by(Subject.name)
        )
        return s.execute(q).all()


def select_10(student_id: int, teacher_id: int):
    with SessionLocal() as s:
        q = (
            select(distinct(Subject.id), Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .where(
                Grade.student_id == student_id,
                Subject.teacher_id == teacher_id,
            )
            .order_by(Subject.name)
        )
        return s.execute(q).all()


def run():
    print("Select 1:", select_1())
    print("Select 2 (subject_id=1):", select_2(1))
    print("Select 3 (subject_id=1):", select_3(1))
    print("Select 4:", select_4())
    print("Select 5 (teacher_id=1):", select_5(1))
    print("Select 6 (group_id=1):", select_6(1))
    print("Select 7 (group_id=1, subject_id=1):", select_7(1, 1))
    print("Select 8 (teacher_id=1):", select_8(1))
    print("Select 9 (student_id=1):", select_9(1))
    print("Select 10 (student_id=1, teacher_id=1):", select_10(1, 1))


if __name__ == "__main__":
    run()
