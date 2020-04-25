from app.app import create_app
from app.config import DevelopConfig

app = create_app(DevelopConfig)
app.run('127.0.0.1', '5000')
