import os


class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAX_NUMBER = os.environ.get('MAX_NUMBER') or '100'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'weplus-test.db'
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True