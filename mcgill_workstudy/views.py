from mcgill_workstudy import app
from flask import Flask, render_template, request
from database import query_db, get_searchable_faculties, get_searchable_terms, workstudy_point_query
from searchForm import WorkstudySearchForm
import psycopg2


@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/about')
def about():
    return 'This is the about page.'


@app.context_processor
def fetch_faculties_and_terms():
    try:
        return dict(searchable_terms = get_searchable_terms(chronological_order = True),
             searchable_faculties = get_searchable_faculties())
    except psycopg2.Error as e:
        print "Executed Code."
        return dict(searchable_terms = None, searchable_faculties = None)


### The following two methods constitute the reference information features
### in this web site.

@app.route('/info/faculties')
def generate_faculties_page():
    return generate_information_page('SELECT * FROM searchable_faculties', 'faculty_listings.html')

@app.route('/info/terms/')
def generate_terms_page():
    return generate_information_page('SELECT * FROM academic_terms', 'term_listings.html')

def generate_information_page(query, template):
    try:
        information_table = query_db(query)
        render_template(template, entries = information_table)
    except psycopg2.Error as e:
        render_template('service_message.html',
                        message = "The requested information could not be retrieved due to a database error.")


### The following three methods constitute the simple searching abilities
### in this web site.

@app.route('/student/<int:student_id>')
def search_by_student_id(student_id):
    return generate_search_results(student_id = student_id)

@app.route('/faculty/<regex("[A-Za-z]{2}"):faculty_id>')
def search_by_faculty_id(faculty_id):
    return generate_search_results(faculty_id = faculty_id)

@app.route('/term/<int:year>/<regex("(fall|winter|summer)"):season>')
def search_by_term(year, season):
    return generate_search_results(term_year = year, term_season = season)


### The next two methods deal with handling multi-term searching in this web site.
@app.route('/advanced_search/')
def render_advanced_search_form():
    return render_template('advanced_search.html')


@app.route('/search')
def process_search_request():
    complex_query = WorkstudySearchForm(request.args)
    if complex_query.validate():
        return generate_search_results(**complex_query.get_search_form_data())
    else:
        return render_template('service_message.html', page_header = "Search Halted",
                        message = "The requested search could not proceed due to invalid search parameters.")


### The following method, 'generate_search_results,' is the heart of the query rendering and displaying.

def generate_search_results(student_id = None, faculty_id = None, term_season = None, term_year = None,
                          status = None, start_date = None, end_date = None):
    try:
        query_results = workstudy_point_query(student_id, faculty_id, term_season, term_year, status, start_date, end_date)
        return render_template('search_results.html', page_header = "Search Results", entries = query_results)
    except psycopg2.Error as e:
        return render_template('service_message.html', page_header = "Search Halted",
                        message = "The requested search could not proceed due to a database error.")
