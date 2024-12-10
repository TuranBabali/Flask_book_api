from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api 



from api.database import db
from api.config.config import config_dict
from api.book.models import Book
from api.book.views import book_namespace


def create_app(config=config_dict['dev']):
    app=Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate=Migrate(app,db)

    api = Api(app,title='Book_store_api')
    api.add_namespace(book_namespace)
    
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db,
                'Book': Book} 
    return app

