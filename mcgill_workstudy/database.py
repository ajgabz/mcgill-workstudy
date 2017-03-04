import psycopg2
from flask import g
from mcgill_workstudy import app
from psycopg2.extras import DictCursor


def connect_db():
    """Connects to the specific database."""
    conn = psycopg2.connect(dbname=app.config['DB_NAME'], user=app.config['DB_USERNAME'], password=app.config['DB_PSWD'])
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

    return query_db('workstudy_point_query', args = (student_id, faculty_id, term_season, term_year, status, start_date,
                                                     end_date), is_stored_procedure = True)

def get_searchable_terms(chronological_order = None):
    return query_db('get_searchable_terms', args = (chronological_order), is_stored_procedure = True)

def get_searchable_faculties():
    """ Retrieves a list of faculty IDs, along with their descriptions, that are housed in the database."""
    return query_db('SELECT * FROM searchable_faculties')

def query_db(query, args = (), is_stored_procedure = False):
    """Fetches a cursor from the DB connection (which is created if need be) and performs the
       given query/stored procedure.  The cursor is immediately closed thereafter. """
    cur = get_db().cursor(cursor_factory=psycopg2.extras.DictCursor)
    if (is_stored_procedure):
        cur.callproc(query, args)
    else:
        cur.execute(query, args)
    entries = cur.fetchall()
    cur.close()
    return entries
