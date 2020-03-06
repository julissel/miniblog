from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


# обработчики маршрутов приложений = функции просмотра

@app.route('/')
@app.route('/index')
def index():
    user = {'username', 'user'}
    posts = [
        {
            'author': {'username': 'Ann'},
            'body': 'How to create chocolate cake'
        },
        {
            'author': {'username': 'Kate'},
            'body': 'New tasty bread'
        },
        {
            'author': {'username': 'Angela'},
            'body': 'Easy way to make jam'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)
