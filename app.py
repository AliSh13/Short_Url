from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from config import DevelopConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(DevelopConfig)
# инициализируем объект БД
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)
lm = LoginManager(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from short.blueprint import short_url
from users.blueprints import users
import view

app.register_blueprint(short_url, url_prefix='/sh')
app.register_blueprint(users, url_prefix='/users')
