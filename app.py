from flask import Flask
from config import Configuration, DevelopConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
import pymysql

from short.blueprint import short_url
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)

app.config.from_object(DevelopConfig)
# инициализируем объект БД
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.register_blueprint(short_url, url_prefix='/sh')
