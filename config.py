import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='safeword'
    DATABASE_URL='postgresql+psycopg2://postgres:787898@localhost/pugpitch'
    UPLOADED_PHOTOS_DEST ='app/static'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # email configurations
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS= False
    MAIL_USE_SSL=True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:787898@localhost/pugpitch'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:787898@localhost/pugpitch'

    DEBUG = True
    ENV = 'development'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
