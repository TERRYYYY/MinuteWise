

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://terry:2002@localhost/minutewise'
    UPLOADED_PHOTOS_DEST ='app/static/photos'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://terry:2002@localhost/minutewise'

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://terry:2002@localhost/minutewise_test'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}