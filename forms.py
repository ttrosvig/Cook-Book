from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired("First name required")],
    render_kw={'autofocus': True})

    last_name = StringField("Last Name", validators=[InputRequired("Last name required")])

    username = StringField("Username", validators=[InputRequired("Username required"), Length(min=5, message="Username must be at least five characters long")])

    password = PasswordField("Password", validators=[InputRequired("Password required"), Length(min=7, message="Password must be at least seven characters")])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired("Username required")],
    render_kw={'autofocus': True})

    password = PasswordField("Password", validators=[InputRequired("Password required")])

class AddRecipeForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired("Recipe title required")],
    render_kw={'autofocus': True})

    body = TextAreaField("Recipe body", validators=[InputRequired('Recipe body required')], 
    render_kw={"rows": 10})