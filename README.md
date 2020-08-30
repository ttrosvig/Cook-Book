# The Cook Book

This is an app that allows a user to securely login, view, add, update and delete their recipes, and recieve random recipe suggestions for those who can't decide or just want something new.

### Tools
This app is built with Flask, HTML, CSS, JS, Bootstrap, and jQuery. PostgreSQL is used as the RDBMS, with Flask-SQLAlchemy working behind the scenes. Flask-Bcrypt is used to hash passwords and keep the login secure, as well as manage authentication and registration. Lastly, WTForms is used for form validation, and Heroku for deployment!

### API
This app utilized the convenience of the [Spoonacular](https://spoonacular.com/food-api) api. I used this API to retrieve a random dessert recipe on button click, which the user can view via link and potentially add to their recipes.

### The Target User
This app was developed to help anyone and everyone store information about what they love most (or second-most)... FOOD. 

### Features
The Cook Book features a stylish home page that displays a random recipe suggestion at the top, followed by a list of recipes entered by the user. Each recipe will include a title that can be clicked to view the recipe. This app features full CRUD functionality, as well as a slick and secure login!

### User Flow
When a user opens the app, they will see homepage, which gives a breif description of the app and what it can do. The user will have the ability to login and see the recipes they stored, as well as their recipe suggestion! The user can click on the recipe container to veiw the actual recipe details. In additon to the recipe itself, this page also provides options to update and delete a recipe.

### Database Schema
The database [schema](schema.png) is relatively simple. There is a user table, which contains user information such as their first name, last name, username and hashed password. This table has a one to many relationship with the recipe table, which includes a recipe id, user_id, title, and recipe body.
