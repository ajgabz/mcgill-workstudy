import os
from flask import Flask
from flask_reggie import Reggie

app = Flask(__name__)

if os.environ.get('HEROKU') is None:
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config')
    app.config['POSTGRES_CONNECTION_URI'] = os.environ["DATABASE_URL"]


Reggie(app)

import mcgill_workstudy.views
import mcgill_workstudy.database
import mcgill_workstudy.searchForm
