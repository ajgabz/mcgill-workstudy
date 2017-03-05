from mcgill_workstudy import app
from flask import Flask, render_template, request
from database import get_searchable_faculties, get_searchable_terms, workstudy_point_query
from searchForm import WorkstudySearchForm
import psycopg2


@app.context_processor
def fetch_faculties_and_terms():
    try:
        return dict(searchable_terms = get_searchable_terms(chronological_order = True),
             searchable_faculties = get_searchable_faculties())
    except psycopg2.Error as e:
        print "*********************************************************************"
        print "Database Error: " + e.message
        print "*********************************************************************"
        return dict(searchable_terms = [], searchable_faculties = [])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/info/faculties')
def faculties_info_page():
    return render_template('faculty_listings.html')


### The following three methods constitute the simple searching abilities
### in this web site.

@app.route('/student/<int:student_id>')
def search_by_student(student_id):
    return generate_search_results(student_id = student_id)

@app.route('/faculty/<regex("[A-Za-z]{2}"):faculty_id>')
def search_by_faculty(faculty_id):
    return generate_search_results(faculty_id = faculty_id)

@app.route('/term/<int:year>/<regex("(?i)(fall|winter|summer)"):season>')
def search_by_term(year, season):
    return generate_search_results(term_year = year, term_season = season)


### The next two methods deal with handling multi-term searching in this web site.
@app.route('/advanced_search/')
def render_advanced_search_form():
    return render_template('service_message.html', page_header = "Advanced Search Unavailable",
                           message = "This feature has not yet been implemented.")
    #return render_template('advanced_search.html')



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
