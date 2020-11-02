import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andrewjohn:andy1234@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andrewjohn:andy1234@localhost/blog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andrewjohn:andy1234@localhost/blog'
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}