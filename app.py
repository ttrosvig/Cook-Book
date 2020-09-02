import os
from flask import Flask, render_template, redirect, session
from models import db, connect_db, User, Recipe
from forms import LoginForm, RegisterForm, AddRecipeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///recipes_db')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Tr1stanT')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

connect_db(app)

@app.route('/')
def home():
    """Renders the basic page for a user that isn't logged in"""

    if "user_id" in session:
        return redirect(f"/home/{session['user_id']}")
        
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    """Retrieves data from the form, stores the data in the database and adds the user to the session (logged in)"""

    if "user_id" in session:
        return redirect(f"/home/{session['user_id']}")

    form = RegisterForm()

    # Retrieve form values
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        # Call the User class method to hash the user password
        user = User.register(username, password, first_name, last_name)

        # Commit changes and add the user to the session
        db.session.commit()
        session['user_id'] = user.id

        return redirect(f"/home/{user.id}")
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Retrieve form data, login the user and add the user to the session, if authenticated"""

    if 'user_id' in session:
        return redirect(f"/home/{session['user_id']}")

    form = LoginForm()

    # Retrieve form values
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Call the User login class method to login the user
        user = User.login(username, password)

        if user:

            # Add the user to the session
            session['user_id'] = user.id
            return redirect(f"/home/{user.id}")
        else:
            form.username.errors = ["Invalid username/password"]

            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/home/<int:user_id>')
def user_home(user_id):
    """Load the page for a logged in user that displays the user's stories. Requires login"""

    # Check if the user is logged in
    if "user_id" not in session or user_id != session['user_id']:
        return redirect('/login')

    # Retrieve the user and the user's recipes
    user = User.query.get(user_id)
    recipe_list = Recipe.query.filter(Recipe.user_id==user.id).order_by(Recipe.title)

    return render_template('user_home.html', user=user, recipe_list=recipe_list)

@app.route('/logout')
def logout():
    """Logout the user by removing their name from the session"""

    session.pop('user_id')

    return redirect('/login')

@app.route('/recipes/add', methods=['GET', 'POST'])
def add_recipe():
    """Retrieve form values, create a recipe instance and add it to the database"""

    # Requires login
    if 'user_id' not in session:
        return redirect('/login')
    
    form = AddRecipeForm()

    # Retrieve form values
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        recipe = Recipe(user_id=session['user_id'], title=title, body=body)

        db.session.add(recipe)
        db.session.commit()

        return redirect(f"/home/{session['user_id']}")

    else:
        return render_template('add_recipe.html', form=form, user_id=session['user_id'])

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    """Displays a form with values inserted to be edited"""

    # Requires login
    if 'user_id' not in session:
        return redirect('/login')

    recipe = Recipe.query.get(recipe_id)

    form = AddRecipeForm(obj=recipe)

    if form.validate_on_submit():
        title = form.body.data
        body = form.body.data

        db.session.commit()

        return redirect(f"/home/{session['user_id']}")

    else:
        return render_template('add_recipe.html', form=form, user_id=session['user_id'])

@app.route('/recipes/<int:recipe_id>/delete')
def delete_recipe(recipe_id):
    """Deletes a recipe"""

    # Requires login
    if 'user_id' not in session:
        return redirect('/login')
        
    recipe = Recipe.query.get(recipe_id)

    db.session.delete(recipe)
    db.session.commit()

    return redirect(f"/home/{session['user_id']}")