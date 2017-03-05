from flask import Flask
from flask_reggie import Reggie


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

Reggie(app)


import mcgill_workstudy.views
import mcgill_workstudy.database
import mcgill_workstudy.searchForm
