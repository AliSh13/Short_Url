# -*- coding: utf-8 -*-
import os
import json
from pathlib import Path
from .utils import INSTANCE_FOLDER_PATH


def make_config(path=None):
    if path is None:
        path = './config.json'
    if not Path(path).exists():
        raise Exception("Файл config.json не найден")
    with open(path, 'r') as conf:
        config = json.load(conf)
    return config


def pg_conn_string(conf: dict):
    return 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=conf['USER'], passwd=conf['PASS'], host=conf['HOST'],
        port=conf.get('PORT', 5432), db=conf['DB_NAME']
        )


class BaseConfig(object):
    PROJECT = "short_link"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shlinksecretkey'
    EXTEND_EXISTINGS = True
    DEBUG = True
    ASSETS_DEBUG = True
    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    TESTING = False
    #MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    #UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 300
    #PRESERVE_CONTEXT_ON_EXCEPTION = False
    #DOWNLOAD_PATH = '/opt/data/dist/'


class DevelopConfig(BaseConfig):
    domain = make_config()["DOMAIN"]
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = pg_conn_string(make_config()["DB"])
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXTEND_EXISTINGS = True
    DEBUG = True
    ASSETS_DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
