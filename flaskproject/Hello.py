from flask import Flask, escape
from datetime import date
app = Flask(__name__)

@app.route('/')
def index():
    return('Index page')

@app.route('/hello')
def hello_world():
    return('Hello, World!')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return('User %s' % escape(username))

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
