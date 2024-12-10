from flask import Flask
from flask_migrate import Migrate

from database import db


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='your_secret_key'

    db.init_app(app)
    migrate=Migrate(app,db)

    return app

