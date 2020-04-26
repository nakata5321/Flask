from flask import Flask
from flask import render_template
from markupsafe import escape
import sqlalchemy as sql

engine = sql.create_engine('postgresql+psycopg2://postgres:mysecretpassword@db:5432/postgres', echo=False)
metadata = sql.MetaData()
information = sql.Table('information', metadata,
     sql.Column('id', sql.Integer, primary_key=True),
     sql.Column('name', sql.String)
     )

metadata.create_all(engine)
conn = engine.connect()

#ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_APP=Hello.py


##############################
app = Flask(__name__)

@app.route('/')
def index():
    return('First page')

@app.route('/site/hello')
def hello_world():
    return('Hello, World!')

@app.route('/site/print')
def print_db():
    result = []
    current_db = conn.execute(sql.select([information]))
    for row in current_db:
        result.append(row)
    return(render_template("database.html", data = result))
#    return('this is check')

@app.route('/site/add/<value>')
def add_information(value):
    conn.execute(information.insert(), name = value)
    return('You have added: %s' % escape(value))
