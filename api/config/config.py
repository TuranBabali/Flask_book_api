from decouple import config


import os

db_name= config('DB_NAME')
db_user= config('DB_USERNAME')
db_password= config('DB_PASSWORD')



class Config:
    SECRET_KEY = config('SECRET_KEY', 'Secret')
    

class DevConfig(Config):
    SQLAlCHEMY_DATABASE_URI = "postgresql://{}:{}@localhost/{}".format(db_user, db_password, db_name)
    SQLALCHEMY_ECHO = True
    DEBUG= config('FLASK_DEBUG',cast=bool)


class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass