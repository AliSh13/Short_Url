from flask import Blueprint
from flask import render_template

short_url = Blueprint('short_url', __name__, template_folder='templates')

@short_url.route('/')
def short():
    return render_template('short_url/short.html')
