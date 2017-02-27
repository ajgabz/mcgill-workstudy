from flask import Flask, request, session, g, redirect, url_for, render_template
import psycopg2
from psycopg2.extras import DictCursor


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

def connect_db():
    """Connects to the specific database."""
    conn = psycopg2.connect(dbname="aarongaba", user="aarongaba", password="")
    #dict_cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
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

@app.route("/")
def index():
    return "Hello world!"

@app.route("/terms/")
def show_terms():
    db = get_db()
    dict_cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dict_cursor.execute("SELECT * FROM Term")
    entries = dict_cursor.fetchall()
    return render_template('show_entries.html', entries=entries)



