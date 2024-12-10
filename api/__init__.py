from flask import Flask
from flask_migrate import Migrate


from api.database import db
from api.config.config import config_dict
from api.book.models import Book


def create_app(config=config_dict['dev']):
    app=Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate=Migrate(app,db)
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db,
                'Book': Book} 

    return app

