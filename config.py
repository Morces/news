

class Config:
    '''
    General configureation parent class
    '''
    pass

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