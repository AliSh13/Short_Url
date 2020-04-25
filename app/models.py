from .app import db
from flask_login import UserMixin


class UsersApp(db.Model, UserMixin):
    '''формирование таблицы пользователей'''
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True, autoincrement=True)
    username = db.Column(db.VARCHAR(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(150))
    url = db.relationship('Urls', backref='username', lazy='dynamic')
    stat = db.relationship('UrlStat', backref='selfuser', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(UsersApp, self).__init__(*args, **kwargs)

    def __str__(self):
        return f'Пользователь - {self.id} {self.username}'

    def __repr__(self):
        return f'<User {self.username}>'


class Urls(db.Model):
    '''формирование таблицы ссылок '''
    __tablename__ = 'urls'

    id = db.Column(db.Integer(), unique=True, autoincrement=True, nullable=False)
    url = db.Column(db.VARCHAR(512), nullable=False)
    sh_url = db.Column(db.VARCHAR(50), nullable=False, unique=True, primary_key=True)
    tag = db.Column(db.VARCHAR(60), nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'),
                        nullable=False)
    stat = db.relationship('UrlStat', backref='selfurl', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Urls, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.sh_url

    def __repr__(self):
        return f"Новая ссылка - {self.sh_url}"


class UrlStat(db.Model):
    """Таблица статистики"""
    __tablename__ = 'statistic'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False, unique=True)
    url_id = db.Column(db.Integer(), db.ForeignKey('urls.id', ondelete='CASCADE'),
                       nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'),
                        nullable=False)
    counter = db.Column(db.INT(), nullable=False, default=0)
    chrome = db.Column(db.INT(), nullable=False, default=0)
    firefox = db.Column(db.INT(), nullable=False, default=0)
    yandex = db.Column(db.INT(), nullable=False, default=0)
    opera = db.Column(db.INT(), nullable=False, default=0)
    other_br = db.Column(db.INT(), nullable=False, default=0)
    android = db.Column(db.INT(), nullable=False, default=0)
    windows = db.Column(db.INT(), nullable=False, default=0)
    mac = db.Column(db.INT(), nullable=False, default=0)
    linux = db.Column(db.INT(), nullable=False, default=0)
    other_pl = db.Column(db.INT(), nullable=False, default=0)
    date_use = db.Column(db.DATETIME(), nullable=False)

    def __init__(self, *args, **kwargs):
        super(UrlStat, self).__init__(*args, **kwargs)

    def __str__(self):
        return f'Статистика по {Urls.sh_url}'
