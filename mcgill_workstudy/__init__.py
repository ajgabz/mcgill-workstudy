from flask import Flask
from flask_reggie import Reggie

app = Flask(__name__)
app.config['DEBUG'] = True

Reggie(app)

#app = Flask(__name__, instance_relative_config=True)
#app.config.from_object('config')
#app.config.from_pyfile('config.py')

#db.Model.metadata.reflect(db.engine)

#from models import db
#db.init_app(app)

import mcgill_workstudy.views
import mcgill_workstudy.database
import mcgill_workstudy.searchForm
