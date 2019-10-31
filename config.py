import os

class Configuration():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URI = 'mysql+mysqlconnector://short_user:1e2w3q2200@localhost/sh_db'


class ProductionConfig(Configuration):
    DEBUG = False


class DevelopConfig(Configuration):
    DEBUG = True
    ASSETS_DEBUG = True
    domain = "http://localhost:5000/"

    host = "localhost"
    user = "short_user"
    password = "1e2w3q2200"
    db = "sh_db"
