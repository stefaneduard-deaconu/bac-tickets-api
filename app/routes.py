from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    pass  # TODO


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Stefan'}
    return render_template('index.html', user=user)