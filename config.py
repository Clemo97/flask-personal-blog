import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'clement'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clement:clemolumz@localhost/blogs'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS =True
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # MAIL_USERNAME = 'oduolpepe618@gmail.com'
    # MAIL_PASSWORD = '37959713Sam'


    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clement:clemolumz@localhost/blogs'

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,

}
