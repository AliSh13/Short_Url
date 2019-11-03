from flask import Flask
from config import Configuration, DevelopConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
import pymysql

from short.blueprint import short_url


app = Flask(__name__)

app.config.from_object(DevelopConfig)
# инициализируем объект БД
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

app.register_blueprint(short_url, url_prefix='/sh')
