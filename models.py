from app import db

class Users(db.Model):
    '''формирование таблицы пользователей'''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password = db.Column(db.String(255))