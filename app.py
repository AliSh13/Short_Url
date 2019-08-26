from flask import Flask
from config import Configuration

from short.blueprint import short_url


app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(short_url, url_prefix='/short')
