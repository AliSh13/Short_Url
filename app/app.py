from flask import Flask
import sys

from app.config import DevelopConfig, make_config, pg_conn_string
from .extensions import db, lm

#from gevent import monkey
#monkey.patch_all()


def create_app(config=None, config_file=None, app_name=None):
    """Create a Flask app."""
    if app_name is None:
        app_name = DevelopConfig.PROJECT
    app = Flask(app_name,
                instance_relative_config=True,
                template_folder='app/templates')
    configure_app(app, config, config_file)
    configure_blueprints(app)
    configure_extensions(app)
    configure_logging(app)
    configure_global_hook(app)
    return app


def configure_app(app, config=None, config_file=None):
    """установка конфига из класса, так же берет коннекты к БД из конфиг файла если он указан"""
    if config_file:
        data = make_config(config_file)
        config.SQLALCHEMY_DATABASE_URI = pg_conn_string(data["DB"])
    if config:
        app.config.from_object(config)
    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)


def configure_extensions(app):
    db.init_app(app)
    lm.init_app(app)


def configure_blueprints(app):
    """Configure blueprints in views."""
    from app.short.blueprint import short_url
    from app.users.blueprints import users

    app.register_blueprint(short_url, url_prefix='/sh')
    app.register_blueprint(users, url_prefix='/users')


def configure_logging(app):
    """Configure file(info) and email(error) logging."""
    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return
    import logging
    import os
    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(handler)


def configure_global_hook(app):
    pass
    # @app.before_request
    # def before_request():
    #     pass
    #
    # @app.after_request
    # def after_request(response):
    #     pass


