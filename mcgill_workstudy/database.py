import psycopg2
from flask import g
from mcgill_workstudy import app
from psycopg2.extras import DictCursor


def connect_db():
    """Connects to the specific database."""
    conn = psycopg2.connect(app.config['POSTGRES_CONNECTION_URI'])
    #conn = psycopg2.connect(dbname=app.config['DB_NAME'], user=app.config['DB_USERNAME'], password=app.config['DB_PSWD'])
    conn.autocommit = True
    return conn

def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    if not hasattr(g, 'postgres_db'):
        g.postgres_db = connect_db()
    return g.postgres_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgres_db'):
        g.postgres_db.close()


def workstudy_point_query(student_id = None, faculty_id = None, term_season = None, term_year = None,
                          status = None, start_date = None, end_date = None):
    """A wrapper function around the workstudy_point_query stored procedure in PostgreSQL."""

    return run_db_procedure('workstudy_point_query',
                            args = [student_id, faculty_id, term_season, term_year, status, start_date, end_date])

def get_searchable_terms(chronological_order = None):
    """A wrapper function around the get_searchable_terms stored procedure in PostgreSQL."""
    return run_db_procedure('get_searchable_terms', args = [chronological_order])

def get_searchable_faculties():
    """ Retrieves a list of faculty IDs, along with their descriptions, that are housed in the database."""
    return run_db_procedure('get_searchable_faculties')

def run_db_procedure(procedure_name, args = None):
    """Fetches a cursor from the DB connection (which is created if need be) and performs the
       given query/stored procedure.  The cursor is immediately closed thereafter. """
    cur = get_db().cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.callproc(procedure_name, args)
    entries = cur.fetchall()
    cur.close()
    return entries
