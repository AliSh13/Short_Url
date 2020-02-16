# -*- coding: utf-8 -*-
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()
db = SQLAlchemy()
lm = LoginManager()