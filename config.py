

from distutils.command.config import config

from instance.config import NEWS_API_KEY


class Config:
    '''
    General configureation parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = 'c8595be1853149d6a6c3547f36c268d0'


    
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