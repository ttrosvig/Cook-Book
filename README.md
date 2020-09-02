# The Cook Book

This is an app that allows a user to securely log in, view, add, update and delete their recipes or recieve random recipe suggestions for those just wanting to try something new. Try it out [here](https://recipe-book-capstone1.herokuapp.com/)!

### Tools
This app is built with Flask, HTML, CSS, JS, Bootstrap, and jQuery. PostgreSQL is used as the RDBMS, with Flask-SQLAlchemy working behind the scenes. Flask-Bcrypt is used to hash passwords and keep the login secure, as well as manage authentication and registration. Lastly, WTForms is used for form validation and Heroku for deployment.

### API
This app utilizes the convenience of the [Spoonacular](https://spoonacular.com/food-api) API. I used this API to retrieve a random dessert recipe on button click, which the user can view via link and potentially add to their recipes.

### The Target User
This app was developed to help the user store information about what some love most...FOOD. 

### Features
The Cook Book features a stylish home page that displays a random recipe suggestion at the top, followed by a list of recipes entered by the user. Each recipe will include a title that can be clicked to view the recipe. This app features full CRUD functionality, as well as a slick and secure login.

### User Flow
When a user opens the app, they will see homepage, which gives a brief description of the app. The user will have the ability to log in and see the recipes they stored, as well as obtain a recipe suggestion. The user can click on the recipe container to veiw the actual recipe details. In additon to the recipe itself, this page also provides options to update and delete a recipe.

### Database Schema
The database [schema](schema.png) is relatively simple. There is a user table, which contains user information such as their first name, last name, username and hashed password. This table has a one to many relationship with the recipe table, which includes a recipe id, user_id, title, and recipe body.
