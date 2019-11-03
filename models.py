from app import db

class Users(db.Model):
    '''формирование таблицы пользователей'''
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password = db.Column(db.String(255))
    url = db.relationship('Urls', backref='user', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __str__(self):
        return f'Пользователь - {self.id} {self.email}'


class Urls(db.Model):
    '''формирование таблицы ссылок '''
    __tablename__ = 'urls'

    id = db.Column(db.Integer(), unique=True, autoincrement=True)
    url = db.Column(db.VARCHAR(512), nullable=False, index=True)
    sh_url = db.Column(db.VARCHAR(50), nullable=False, unique=True, primary_key=True)
    tag = db.Column(db.VARCHAR(60), nullable=True, index=True)
    user = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    stat = db.relationship('UrlStat', backref='url', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Urls, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.sh_url

    def __repr__(self):
        return f"Новая ссылка - {self.sh_url}"

class UrlStat(db.Model):
    """Таблица статистики"""
    __tablename__ = 'statistic'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    url = db.Column(db.Integer(), db.ForeignKey('urls.id'), nullable=False)
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
