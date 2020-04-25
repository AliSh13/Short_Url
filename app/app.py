import sys
from flask import render_template
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.config import DevelopConfig, make_config, pg_conn_string
from .extensions import db, lm

#from gevent import monkey
#monkey.patch_all()


def create_app(config=None, config_file=None, app_name=None):
    """Create a Flask app."""
    if app_name is None:
        app_name = DevelopConfig.PROJECT
    app = Flask(app_name, template_folder='templates')
    configure_app(app, config, config_file)
    configure_blueprints(app)
    configure_extensions(app)
    configure_logging(app)
    configure_admin(app)

    @app.route('/')
    def index():
        return render_template('index.html')

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


def configure_blueprints(app_fl):
    """Configure blueprints in views."""
    from app.short.blueprint import short_url
    from app.users.blueprints import users

    app_fl.register_blueprint(short_url, url_prefix='/sh')
    app_fl.register_blueprint(users, url_prefix='/users')


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


def configure_admin(app_fl):
    from .models import Urls, UrlStat, UsersApp
    from app.admin.blueprint import AnalyticsView
    app_fl.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app_fl, name=app_fl.name, template_mode='bootstrap3')

    class UserModelView(ModelView):
        column_default_sort = 'Username'
        column_list = ('Username', 'Email')
        column_searchable_list = ('Username', 'Email')

    admin.add_view(ModelView(UsersApp, db.session))
    admin.add_view(ModelView(UrlStat, db.session, category="links"))
    admin.add_view(ModelView(Urls, db.session, category="links"))
    admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))


