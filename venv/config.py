import os
from typing import Any, Union


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'try-to-gues-what'
