from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://aarongaba:@localhost/aarongaba"
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG'] = True

#app = Flask(__name__, instance_relative_config=True)
#app.config.from_object('config')
#app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
#db.Model.metadata.reflect(db.engine)

#from models import db
#db.init_app(app)

import mcgill_workstudy.views
