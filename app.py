from flask import Flask, render_template
from models import db, connect_db, User, Recipe

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///recipes_db'

app.config['SECRET_KEY'] = 'SECRET'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

connect_db(app)

@app.route('/')
def home():
    return render_template('index.html')