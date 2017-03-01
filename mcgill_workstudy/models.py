from mcgill_workstudy import db
import enum


class Faculty(db.Model):
    __tablename__ = 'faculty'

    faculty_id = db.Column('facultyid', db.String(2), primary_key=True)
    description = db.Column('description', db.String(32), nullable=False)


class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column('studentid', db.Integer, primary_key=True)


class Term(db.Model):
    __tablename__ = 'term'

    semester_term = db.Column('semesterterm', db.Enum(u'Winter', u'Summer', u'Fall', name='semester'), primary_key=True, nullable=False)
    term_year = db.Column('termyear', db.Integer, primary_key=True, nullable=False)
    term_start = db.Column('termstart', db.Date, nullable=False)
    term_end = db.Column('termend', db.Date, nullable=False)

class Work_Study_Application(db.Model):
    __tablename__ = 'application'

    student_id = db.Column('studentid', db.Integer, primary_key=True)
    semester_term = db.Column('')