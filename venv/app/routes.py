# -*- coding: utf-8 -*-
from flask import render_template
from app import app


# обработчики маршрутов приложений = функции просмотра

@app.route('/')
@app.route('/index')
def index():
    new_user = {'username', 'new_user'}
    return render_template('index.html', title='Main page', user=new_user)
