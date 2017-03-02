from mcgill_workstudy import app
from flask import Flask, render_template, request
from database import query_db
from searchForm import construct_single_term_query, WorkstudySearchForm
import psycopg2


@app.route('/')
def home():
    return 'This is the home page'


### The following three methods constitute the simple searching abilities
### in this web site.


@app.route('/student/<int:student_id>')
def search_by_student_id(student_id):
    return generate_search_results(*construct_single_term_query("studentid", student_id))

@app.route('/faculty/<regex("[A-Za-z]{2}"):faculty_id>')
def search_by_faculty_id(faculty_id):
    return generate_search_results(*construct_single_term_query("facultyid", faculty_id))

@app.route('/term/<int:year>/<regex("(fall|winter|summer)"):semester>')
def search_by_term(year, semester):
    complex_query = WorkstudySearchForm({'termyear': year, 'semesterterm': semester})
    return generate_search_results(*complex_query.construct_query())

### The next two methods deal with handling multi-term searching in this web site.

@app.route('/advanced_search/')
def render_advanced_form():
    return render_template('advanced_search.html', page_header = "Advanced Search")

@app.route('/search')
def process_search_request():
    complex_query = WorkstudySearchForm(request.args)
    if complex_query.validate():
        return generate_search_results(*complex_query.construct_query())
    else:
        return render_template('service_message.html', page_header = "Search Halted",
                        message = "The requested search could not proceed due to invalid search parameters.")


def generate_search_results(search_query, parameters=[]):
    try:
        query_results = query_db(search_query, parameters)
        return render_template('search_results.html', page_header = "Search Results", entries = query_results)
    except psycopg2.Error as e:
        return render_template('service_message.html', page_header = "Search Halted",
                        message = "The requested search could not proceed due to a database error.")
