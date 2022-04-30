

from distutils.command.config import config


class Config:
    '''
    General configureation parent class
    '''
    

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class 
    '''
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}