import psycopg2
from flask import g
from mcgill_workstudy import app
from psycopg2.extras import DictCursor


def connect_db():
    """Connects to the specific database."""
    conn = psycopg2.connect(dbname="aarongaba", user="aarongaba", password="")
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

def query_db(query, args = ()):
    """Fetches a cursor from the DB connection (which is created if need be) and performs the
       given query.  The cursor is immediately closed thereafter. """
    dict_cursor = get_db().cursor(cursor_factory=psycopg2.extras.DictCursor)
    dict_cursor.execute(query, args)
    entries = dict_cursor.fetchall()
    dict_cursor.close()
    return entries
