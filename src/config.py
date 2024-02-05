from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = True
    HOST = "0.0.0.0"
    SQLALCHEMY_DATABASE_URI = config('MYSQL_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'config': Config
}