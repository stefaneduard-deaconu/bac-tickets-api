from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    pass  # TODO


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Stefan'}
    return render_template('index.html', user=user)