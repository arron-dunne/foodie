# Foodie
The online recipe manager to save and store all your recipes!
- [**Video Demo**](https://youtube.com/watch?v=yu_pxmD6JPU)

- [**Live Deployment**](https://myfoodie.pythonanywhere.com)

## Description
Foodie is a digital recipe book that allows you to add, store and view all your recipes - anytime, anywhere. Each user has a personal account and recipe book. Register a new account to get started, or use the guest account to get a feel for the app.

After logging in, users are shown the *Homepage*, from here you can go to the *Add Recipe* page, which shows a form to fill out with recipe details. The form is very flexible and supports any number of ingredients and steps, as well as a picture of your recipe.

After adding recipes, you can go to the *My Recipes* page to see a list of all your recipes in one place, with a summary. Click on any of the recipes card to view the entire recipe. Users can also edit recipes by clicking the *Edit Button* when viewing a recipe. Changes are updated to the database instantly.

As well as recipes, Foodie keeps track of a shopping list for you. This digital shopping list makes it very easy to add any items you want, and save and view them easily. There is also a feature to add all ingredients from a recipe to your shopping list! 
Clicking the Foodie icon on the navbar will take the user back to the homepage.

If a user is not logged in they will not be able to access any other pages except the *Login* and *Register* pages. 
All data is saved in database. Security measures such as password hashing and SQL escaping have been used to protect user data. 

The Foodie app is written in Python with the Flask framework. The webpages are created with HTML, CSS and Javascript, and use the Bootstrap and JQuery libraries to add functionality. 

There are many features that could be added to Foodie to make it a better app, I plan to continue the development of Foodie into the future.

## Development

The main application code is in the `app.py` file. This initilaised the flask app and contains all the URL endpoints. It also sets up and executes SQL statements to the connected database, which is in the `database.db` file.

For the web deign I used the bootstrap library to have access to lots of ready-made web components. I imported the boostrap library to my web pages inside the `layout.html` file. This file is the template for all other web pages, so having links in here made them accessible to all other HTML files. 
I also imported the JQuery libary, and a link to my CSS file `style.css`. The JQuery library helped my make dynamic pages such as dynamically adding and removing ingredient fields in the `Add Recipe` form.

## Project Structure
- `templates/` contains all the HTML files which are rendered to the user
- `scripts/` contains SQL scripts which can be run on the database to create tables (`start.sql`), and add data (`data.sql`)
- `docs/` contains the database schema design and a manual test plan.
- `static/` contains the CSS styling as well as images, such as the logo
- `static/uploads/` contains the images uploaded by users for their recipes


*Note: I have designed Foodie to be as secure as possible, but please dont share any personal or sensitive information on it*
