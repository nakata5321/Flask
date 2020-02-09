from flask import Flask, escape
from datetime import date
app = Flask(__name__)

@app.route('/')
def index():
    return('Index page')

@app.route('/')
def index2():
    return('index2')


@app.route('/hello')
def hello_world():
    return('Hello, World!')

@app.route('/user/<nakata>')
def show_user_profile(nakata):
    # show the user profile for that user
    pr('User %s' % escape(nakata))
    return("HEllo, nakata!")
