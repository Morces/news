
import os

# from instance.config import SECRET_KEY


class Config:
    '''
    General configureation parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c8595be1853149d6a6c3547f36c268d0'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?&apiKey=c8595be1853149d6a6c3547f36c268d0'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') 


    
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    Debug = False

class DevConfig(Config):
    '''
    Development configuration child class 
    '''
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}