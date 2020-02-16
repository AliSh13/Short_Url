from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[Email()])
    password = PasswordField('Пароль', validators=InputRequired())
    password2 = PasswordField('Повторите пароль', validators=EqualTo('password', message='Пароли не совпадают'))
    submit = SubmitField("регистрация")


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
