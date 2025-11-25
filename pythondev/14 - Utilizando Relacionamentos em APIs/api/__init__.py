import pymysql
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Corrige driver do MySQL no Windows
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)

from .views import curso_views, formacao_views, professor_view
from .models import curso_model, formacao_model, professor_model
