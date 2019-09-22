from flask import Blueprint, render_template, request
from .forms import Shortner

short_url = Blueprint('short_url', __name__, template_folder='templates')

@short_url.route('/')
def short():
    form = Shortner()

    return render_template('short_url/short.html', form = form)
