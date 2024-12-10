from decouple import config


import os

BASE_DIR= os.path.dirname(os.path.realpath(__file__))

db_name= config('DB_NAME')
db_user= config('DB_USERNAME')
db_password= config('DB_PASSWORD')



class Config:
    SECRET_KEY = config('SECRET_KEY', 'Secret')
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = True
    DEBUG= config('FLASK_DEBUG',cast=bool)


class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass



config_dict={
    'dev':DevConfig,
    'test':TestConfig,
    'production':ProdConfig,
}