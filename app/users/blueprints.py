from flask import render_template, Blueprint, redirect, flash, url_for, request
from flask_login import login_user, logout_user, login_required

from .forms import RegisterForm, LoginForm
from .lib import generate_hash, check_hash
from app.models import Users

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate_on_submit():
            user = Users(
                username=form.username.data,
                email=form.email.data,
                password=generate_hash(form.password.data)
            )

            login_user(user)

            # flash('A confirmation email has been sent via email.', 'success')
            return redirect(url_for("index"))
    form = RegisterForm()
    return render_template('users/register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Users.quert.filter_by(email=form.email.data).first()
        if user and check_hash(form.password.data, user.password):
            login_user(user)
            flash('Welcome.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('users/login.html', form=form)
    form = LoginForm()
    return render_template('users/login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.', 'success')
    return redirect(url_for('index'))
