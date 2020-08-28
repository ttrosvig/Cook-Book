from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
        autoincrement=True,
        primary_key=True, 
        nullable=False)

    username = db.Column(db.String,
        nullable=False)

    first_name = db.Column(db.String,
        nullable=False)

    last_name = db.Column(db.String,
        nullable=False)

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False)

    user_id = db.Column(db.Integer,
        db.ForeignKey('users.id'),
        nullable=False)

    title = db.Column(db.String,
        nullable=False)

    body = db.Column(db.Text,
        nullable=False)

    rating = db.Column(db.Integer)