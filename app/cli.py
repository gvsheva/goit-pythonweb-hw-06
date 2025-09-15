#!/usr/bin/env python

import argparse
import sys
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect

from app.db import SessionLocal
from app.models import Group, Teacher, Subject, Student, Grade


def model_columns(instance):
    return [c.key for c in inspect(instance).mapper.column_attrs]


def row_to_dict(instance):
    cols = model_columns(instance)
    return {k: getattr(instance, k) for k in cols}


def print_rows(rows):
    if not rows:
        print("[]")
        return
    for r in rows:
        print(row_to_dict(r))


def teachers_create(args):
    with SessionLocal() as s:
        obj = Teacher(full_name=args.name)
        s.add(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def teachers_update(args):
    with SessionLocal() as s:
        obj = s.get(Teacher, args.id)
        if not obj:
            sys.exit(f"Teacher id={args.id} not found")
        obj.full_name = args.name
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def teachers_list(_args):
    with SessionLocal() as s:
        rows = s.scalars(select(Teacher)).all()
        print_rows(rows)


def teachers_remove(args):
    with SessionLocal() as s:
        obj = s.get(Teacher, args.id)
        if not obj:
            sys.exit(f"Teacher id={args.id} not found")
        s.delete(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        print(f"Deleted Teacher id={args.id}")


def groups_create(args):
    with SessionLocal() as s:
        obj = Group(name=args.name)
        s.add(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def groups_update(args):
    with SessionLocal() as s:
        obj = s.get(Group, args.id)
        if not obj:
            sys.exit(f"Group id={args.id} not found")
        obj.name = args.name
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def groups_list(_args):
    with SessionLocal() as s:
        rows = s.scalars(select(Group)).all()
        print_rows(rows)


def groups_remove(args):
    with SessionLocal() as s:
        obj = s.get(Group, args.id)
        if not obj:
            sys.exit(f"Group id={args.id} not found")
        s.delete(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        print(f"Deleted Group id={args.id}")


def subjects_create(args):
    with SessionLocal() as s:
        obj = Subject(name=args.name, teacher_id=args.teacher_id)
        s.add(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def subjects_update(args):
    with SessionLocal() as s:
        obj = s.get(Subject, args.id)
        if not obj:
            sys.exit(f"Subject id={args.id} not found")
        if args.name is not None:
            obj.name = args.name
        if args.teacher_id is not None:
            obj.teacher_id = args.teacher_id
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def subjects_list(_args):
    with SessionLocal() as s:
        rows = s.scalars(select(Subject)).all()
        print_rows(rows)


def subjects_remove(args):
    with SessionLocal() as s:
        obj = s.get(Subject, args.id)
        if not obj:
            sys.exit(f"Subject id={args.id} not found")
        s.delete(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        print(f"Deleted Subject id={args.id}")


def students_create(args):
    with SessionLocal() as s:
        obj = Student(full_name=args.full_name, group_id=args.group_id)
        s.add(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def students_update(args):
    with SessionLocal() as s:
        obj = s.get(Student, args.id)
        if not obj:
            sys.exit(f"Student id={args.id} not found")
        if args.full_name is not None:
            obj.full_name = args.full_name
        if args.group_id is not None:
            obj.group_id = args.group_id
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def students_list(_args):
    with SessionLocal() as s:
        rows = s.scalars(select(Student)).all()
        print_rows(rows)


def students_remove(args):
    with SessionLocal() as s:
        obj = s.get(Student, args.id)
        if not obj:
            sys.exit(f"Student id={args.id} not found")
        s.delete(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        print(f"Deleted Student id={args.id}")


def grades_create(args):
    with SessionLocal() as s:
        obj = Grade(
            student_id=args.student_id, subject_id=args.subject_id, value=args.value
        )
        s.add(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def grades_update(args):
    with SessionLocal() as s:
        obj = s.get(Grade, args.id)
        if not obj:
            sys.exit(f"Grade id={args.id} not found")
        if args.student_id is not None:
            obj.student_id = args.student_id
        if args.subject_id is not None:
            obj.subject_id = args.subject_id
        if args.value is not None:
            obj.value = args.value
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        s.refresh(obj)
        print(row_to_dict(obj))


def grades_list(_args):
    with SessionLocal() as s:
        rows = s.scalars(select(Grade)).all()
        print_rows(rows)


def grades_remove(args):
    with SessionLocal() as s:
        obj = s.get(Grade, args.id)
        if not obj:
            sys.exit(f"Grade id={args.id} not found")
        s.delete(obj)
        try:
            s.commit()
        except IntegrityError as e:
            s.rollback()
            sys.exit(f"Integrity error: {e.orig}")
        print(f"Deleted Grade id={args.id}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    sp_resources = p.add_subparsers(dest="resource", required=True)

    p_teachers = sp_resources.add_parser("teachers", help="Teachers operations")
    sp_teachers = p_teachers.add_subparsers(dest="action", required=True)

    t_create = sp_teachers.add_parser("create", help="Create a teacher")
    t_create.add_argument("name", help="Teacher's full name")
    t_create.set_defaults(func=teachers_create)

    t_update = sp_teachers.add_parser("update", help="Update a teacher")
    t_update.add_argument("id", type=int)
    t_update.add_argument("name")
    t_update.set_defaults(func=teachers_update)

    t_list = sp_teachers.add_parser("list", help="List all teachers")
    t_list.set_defaults(func=teachers_list)

    t_remove = sp_teachers.add_parser("remove", help="Remove a teacher")
    t_remove.add_argument("id", type=int)
    t_remove.set_defaults(func=teachers_remove)

    p_groups = sp_resources.add_parser("groups", help="Groups operations")
    sp_groups = p_groups.add_subparsers(dest="action", required=True)

    g_create = sp_groups.add_parser("create", help="Create a group")
    g_create.add_argument("name")
    g_create.set_defaults(func=groups_create)

    g_update = sp_groups.add_parser("update", help="Update a group")
    g_update.add_argument("id", type=int)
    g_update.add_argument("name")
    g_update.set_defaults(func=groups_update)

    g_list = sp_groups.add_parser("list", help="List all groups")
    g_list.set_defaults(func=groups_list)

    g_remove = sp_groups.add_parser("remove", help="Remove a group")
    g_remove.add_argument("id", type=int)
    g_remove.set_defaults(func=groups_remove)

    p_subjects = sp_resources.add_parser("subjects", help="Subjects operations")
    sp_subjects = p_subjects.add_subparsers(dest="action", required=True)

    s_create = sp_subjects.add_parser("create", help="Create a subject")
    s_create.add_argument("name")
    s_create.add_argument("teacher_id", type=int)
    s_create.set_defaults(func=subjects_create)

    s_update = sp_subjects.add_parser("update", help="Update a subject")
    s_update.add_argument("id", type=int)
    s_update.add_argument("--name")
    s_update.add_argument("--teacher_id", type=int)
    s_update.set_defaults(func=subjects_update)

    s_list = sp_subjects.add_parser("list", help="List all subjects")
    s_list.set_defaults(func=subjects_list)

    s_remove = sp_subjects.add_parser("remove", help="Remove a subject")
    s_remove.add_argument("id", type=int)
    s_remove.set_defaults(func=subjects_remove)

    p_students = sp_resources.add_parser("students", help="Students operations")
    sp_students = p_students.add_subparsers(dest="action", required=True)

    st_create = sp_students.add_parser("create", help="Crеate a student")
    st_create.add_argument("full_name")
    st_create.add_argument("group_id", type=int)
    st_create.set_defaults(func=students_create)

    st_update = sp_students.add_parser("update", help="Update a student")
    st_update.add_argument("id", type=int)
    st_update.add_argument("--full_name")
    st_update.add_argument("--group_id", type=int)
    st_update.set_defaults(func=students_update)

    st_list = sp_students.add_parser("list", help="List all students")
    st_list.set_defaults(func=students_list)

    st_remove = sp_students.add_parser("remove", help="Remove a student")
    st_remove.add_argument("id", type=int)
    st_remove.set_defaults(func=students_remove)

    p_grades = sp_resources.add_parser("grades", help="Grades operations")
    sp_grades = p_grades.add_subparsers(dest="action", required=True)

    gr_create = sp_grades.add_parser("create", help="Crеate a grade")
    gr_create.add_argument("student_id", type=int)
    gr_create.add_argument("subject_id", type=int)
    gr_create.add_argument("value", type=int)
    gr_create.set_defaults(func=grades_create)

    gr_update = sp_grades.add_parser("update", help="Update a grade")
    gr_update.add_argument("id", type=int)
    gr_update.add_argument("--student_id", type=int)
    gr_update.add_argument("--subject_id", type=int)
    gr_update.add_argument("--value", type=int)
    gr_update.set_defaults(func=grades_update)

    gr_list = sp_grades.add_parser("list", help="List all grades")
    gr_list.set_defaults(func=grades_list)

    gr_remove = sp_grades.add_parser("remove", help="Remove a grade")
    gr_remove.add_argument("id", type=int)
    gr_remove.set_defaults(func=grades_remove)

    return p


def run():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    run()
