from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Введите логин')])
    email = StringField('Электронная почта', validators=[Email('Введите email')])
    password = PasswordField('Пароль', validators=[InputRequired('Введите пароль.')])
    password2 = PasswordField('Повторите пароль', validators=[EqualTo('password', message='Пароли не совпадают')])
    remember_me = BooleanField('запомнить')
    submit = SubmitField("регистрация")


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("Войти")