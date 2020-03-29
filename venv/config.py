import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'try-to-gues-what'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'admin@example.com' # input real email
    MAIL_PASSWORD = 'admin_pass' # input real password
    ADMINS = ['admin@example.com'] # input real email
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'ru']
