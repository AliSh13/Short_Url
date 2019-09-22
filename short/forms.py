from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Shortner(FlaskForm):
    URL = StringField('Ссылка', validators=[DataRequired()])
    shortner_name = PasswordField('Имя для вашей ссылки', validators=[DataRequired()])
    submit = SubmitField('Генерировать')
