from flask import Blueprint, render_template, request, flash
from .forms import Shortner

short_url = Blueprint('short_url', __name__, template_folder='templates')

@short_url.route('/', methods=['GET', 'POST'])
def short():
    form = Shortner()
    if form.validate_on_submit():
        value = form.shortner_name.data
        flash('Новая ссылка готова - sh.su/{}'.format(value))
    return render_template('short_url/short.html', form = form)
