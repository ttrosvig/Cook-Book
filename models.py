from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
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

    password = db.Column(db.String,
        nullable=False)

    first_name = db.Column(db.String,
        nullable=False)

    last_name = db.Column(db.String,
        nullable=False)

    recipes = db.relationship('Recipe', backref='users', cascade="all, delete")

    @classmethod
    def register(cls, username, password, first_name, last_name):

        hashed = bcrypt.generate_password_hash(password)

        hashed_utf8 = hashed.decode('utf8')

        user = cls(
            username = username,
            password = hashed_utf8,
            first_name = first_name,
            last_name = last_name
        )

        db.session.add(user)
        return user

    @classmethod
    def login(cls, username, password):
        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False

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