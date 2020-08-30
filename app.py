from flask import Flask, render_template, redirect, session
from models import db, connect_db, User, Recipe
from forms import LoginForm, RegisterForm, AddRecipeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///recipes_db'

app.config['SECRET_KEY'] = 'SECRET'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

connect_db(app)

@app.route('/')
def home():
    if "user_id" in session:
        return redirect(f"/home/{session['user_id']}")
        
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(f"/home/{session['user_id']}")

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, first_name, last_name)

        db.session.commit()
        session['user_id'] = user.id

        return redirect(f"/home/{user.id}")
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    if 'user_id' in session:
        return redirect(f"/home/{session['user_id']}")

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.login(username, password)

        if user:
            session['user_id'] = user.id
            return redirect(f"/home/{user.id}")
        else:
            form.username.errors = ["Invalid username/password"]

            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/home/<int:user_id>')
def user_home(user_id):
    if "user_id" not in session or user_id != session['user_id']:
        return redirect('/login')

    user = User.query.get(user_id)

    return render_template('user_home.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id')

    return redirect('/login')

@app.route('/recipes/add', methods=['GET', 'POST'])
def add_recipe():
    form = AddRecipeForm()

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
    if 'user_id' not in session:
        return redirect('/login')
        
    recipe = Recipe.query.get(recipe_id)

    db.session.delete(recipe)
    db.session.commit()

    return redirect(f"/home/{session['user_id']}")