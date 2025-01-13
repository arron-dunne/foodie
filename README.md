# FOODIE
#### Video Demo:  https://www.youtube.com/watch?v=yu_pxmD6JPU
#### Description:
Foodie is a digital recipe book that allows you to add, store and view all your recipes anytime, anywhere using the internet. 
Foodie supports user accounts so that each user has their own private recipe book. 
The main use of Foodie is keeping track of your recipes. From the homepage users can go to the 'Add Recipe' page, where they will be shown a form to fill out with their recipe details. The form is very flexible and supports any number of ingredients and steps, as well as a picture of your recipe.
After adding recipes, you can go to the 'My Recipes' page to see a list of all your recipes with a snippet of information. Click on any of the recipes card to view the entire recipe, which you can then follow. 
When viewing a recipe its also possible to edit your recipe, changing any of the details for it on the fly.
As well as recipes, Foodie keeps track of a shopping list for you. This digital shopping list makes it very easy to add any items you want, and save and view them easily. There is also a feature to add all ingredients from a recipe to your shopping list! 
Clicking the Foodie icon on the navbar will always take users back to the homepage.
If a user is not logged in they will not be able to access any other pages except login and register. 
All data is saved in database so it is persistent. Security measures such as password hashing and sql escaping have been used to protect user data. 
The Foodie app is written in Python with the Flask framework. The webpages are created with HTML, CSS and Javascript, and use the Bootstrap and JQuery libraries to add functionality. 
There are many features that could be added to Foodie to make it a better app, I plan to continue the development of Foodie into the future.

The main application code is in the main.py file. This initilaised the flask app and contains all the routing logic. It also sets up and exectures SQL statements to the connected database, which is in the database.db file. Some additional function are stores in the filter.py file.

For the web deign I used bootstrap to have access to lots of ready made, good looking web components. I imported the boostrap library to my web pages inside the layout.html file. This file is the template for all other web pages, so having links in here made them accessible through the entire app. Inside the layout.html I also imported the JQuery libary, to provide reponsive wepages, and links to my CSS file style.css

Most of the other file are for the web pages. Inside templates folder are all the html pages which are loaded from certain URLs. THe index.html file contins the homepage. The hompage contains 3 links with images that link to 'My Recipes', 'Add Recipe' and 'Shopping List' pages. The are animated using CSS to enlarge when a user hovers over them. 

The addrecipe.html file contains a form for adding new recipes. This is a bootstrap form and laid out in a bootstrap grid so all items alligned. It used a mixture of input fields including, text, number and spans as well as a file input for uploading pictures. Users can dynamically add or delete ingredients and step fields using the buttons on this page. The buttons trigger javascript functions in the script part of the file, which updated the html to add or remove fields without having to reload the page.

You can access Foodie at TODO. Simply create an account to get started. But please dont share any personal or sensitive information on it.
