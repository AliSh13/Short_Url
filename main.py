from app.app import db, create_app
from app.config import DevelopConfig
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

if __name__ == '__main__':
    app = create_app(DevelopConfig)

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    app.run()