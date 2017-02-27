from mcgill_workstudy import app, db
from collections import namedtuple
#from models import Student

from flask import Flask, render_template
#from models import db

@app.route('/testdb')
def testdb():
    if db.session.query("semesterterm").from_statement("SELECT * FROM term").all():
        return "It works!"
    else:
        return "Something is broken."

@app.route("/terms/")
def show_terms():
    test_query = db.session.execute('SELECT * FROM term ORDER BY termyear DESC, semesterterm DESC')
    return render_template('show_entries.html', entries=test_query)

@app.route("/students/")
def test_student_query():
    test_query = db.session.execute('SELECT * FROM student ORDER BY studentid')
    return render_template('show_students.html', entries=test_query)

    #result = Student.query.filter_by(Student.c.studentid < 200000000).first()
    #return str(result)