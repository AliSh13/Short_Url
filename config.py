import os

class Configuration():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sh_admin:sh_pas2200@localhost/shor_url'


class ProductionConfig(Configuration):
    DEBUG = False


class DevelopConfig(Configuration):
    DEBUG = True
    ASSETS_DEBUG = True