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

@app.route('/search')
def show_advanced_search():
    return render_template('advanced_search.html', page_header = "Advanced Search")

@app.route("/info/faculties/")
def show_faculties():
    query = db.session.execute('SELECT * FROM faculty ORDER BY facultyid')
    return render_template('faculty_listings.html', page_header = "Faculties", entries = query)

@app.route("/info/terms/")
def show_terms():
    query = db.session.execute('SELECT * FROM term ORDER BY termyear, semesterterm')
    return render_template('term_listings.html', page_header = "Term Information", entries = query)

@app.route("/students/")
def test_student_query():
    test_query = db.session.execute('SELECT * FROM student ORDER BY studentid')
    return render_template('show_students.html', entries=test_query)

    #result = Student.query.filter_by(Student.c.studentid < 200000000).first()
    #return str(result)

@app.route("/student/id/<int:student_id>")
def test_student_query2(student_id):
    test_query = db.session.execute('SELECT * FROM student WHERE studentid = ' + str(student_id))
    return render_template('show_students.html', entries=test_query)
