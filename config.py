import os
import json
from pathlib import Path


def make_config(path=None):
    if path is None:
        path = 'config.json'
    if not Path(path).exists():
        raise Exception("Файл config.json не найден")
    with open(path, 'r') as conf:
        config = json.load(conf)
    return config


def pg_conn_string(conf: dict):
    return f'mysql+pymysql://{conf["USER"]}:{conf["PASS"]}@{conf["HOST"]}/{conf["DB_NAME"]}'


class DevelopConfig():
    domain = make_config()["DOMAIN"]
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = pg_conn_string(make_config()["DB"])
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXTEND_EXISTINGS = True
    DEBUG = True
    ASSETS_DEBUG = True


class ProductionConfig(DevelopConfig):
    DEBUG = False
