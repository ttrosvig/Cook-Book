from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired("First name required")])

    last_name = StringField("Last Name", validators=[InputRequired("Last name required")])

    username = StringField("Username", validators=[InputRequired("Username required"), Length(min=5, message="Username must be at least five characters long")])

    password = PasswordField("Password", validators=[InputRequired("Password required"), Length(min=7, message="Password must be at least seven characters")])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired("Username required")])

    password = PasswordField("Password", validators=[InputRequired("Password required")])