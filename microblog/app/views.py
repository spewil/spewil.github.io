from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
def reader():
	page = {'title': 'test sketch'}
	return render_template('read.html',
							page = page)