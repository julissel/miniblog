from flask import Flask

app = Flask(__name__)
from app import routes  # обходной путь для циклического импорта
