import os

class Config(object):
    SEKRET_KEY = os.environ.get('SECRET_KEY') or 'try-to-gues-what'
