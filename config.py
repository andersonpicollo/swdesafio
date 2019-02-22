# -*- coding: utf-8 -*-

class Config:
    
    PORT = 5000
    DEBUG = True
    MONGODB_HOST = "mongodb://localhost:27017/sw_universe"
    
    

    
class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST="mongodb://localhost:27017/sw_universe"

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}