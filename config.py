import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andrewjohn:andy1234@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


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