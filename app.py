import sqlite3
import os
import functools
from flask import Flask, render_template, request, session, redirect
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from uuid import uuid4


# Start flask app
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.jinja_env.filters['norm'] = lambda num: '{:.0f}'.format(num) # normalize units
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static/uploads")
app.config['DATABASE_URL'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")

# Start database connection
con = sqlite3.connect(app.config['DATABASE_URL'], check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()


# HELPER FUNCTIONS
def get_recipe_info(id):
    recipe = cur.execute("SELECT * FROM recipes WHERE id = ?", (id,)).fetchone()
    ingredients = cur.execute("SELECT ingredient, quantity, units FROM ingredients WHERE recipe_id = ?", (id,)).fetchall()
    steps = cur.execute("SELECT step FROM steps WHERE recipe_id = ?", (id,)).fetchall()
    pictures = cur.execute("SELECT filename FROM pictures WHERE recipe_id = ?", (id,)).fetchall()

    return recipe, ingredients, steps, pictures


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        # If user is not logged in, redirect to login
        if "username" not in session:
            return redirect("/login")
        return view(**kwargs)

    return wrapped_view


def user_specific(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        # Access user_id parameter using request.view_args
        user_id = request.view_args.get('user_id')
        # If user_id in endpoint is not the same as user_id in session, redirect to home
        if user_id != session['user_id']:
            return redirect("/")
        return view(**kwargs)
    
    return wrapped_view


# ROUNTING FUNCTIONS
@app.route("/")
@login_required
def home():
    print(session)
    print(session['user_id'])
    print(type(session['user_id']))
    return render_template("index.html")


@app.route("/list/<user_id>")
@login_required
@user_specific
def list(user_id):
    list = cur.execute("SELECT * FROM list WHERE user_id = ?", (session["user_id"],)).fetchall()

    return render_template("list.html", list=list)


@app.route("/editlist/<user_id>", methods=["GET", "POST"])
@login_required
@user_specific
def editlist(user_id):

    if request.method == "POST":

        item_count = 0

        # Remove old list
        cur.execute("DELETE FROM list WHERE user_id = ?", (session["user_id"],))
        con.commit()

        # Add new items to list
        for item in request.form.getlist("item"):

            # Get the quantity and units for items
            quantity = request.form.getlist("quantity")[item_count]
            units = request.form.getlist("units")[item_count]

            cur.execute("INSERT INTO list (user_id, item, quantity, units) VALUES (?, ?, ?, ?)", (session["user_id"], item, quantity, units))
            con.commit()

            item_count += 1

        return redirect(f"/list/{session['user_id']}")

    else:
        list = cur.execute("SELECT * FROM list WHERE user_id = ?", (session["user_id"],)).fetchall()
        return render_template("editlist.html", list=list)


@app.route("/clearlist/<user_id>")
@login_required
@user_specific
def clearlist(user_id):

    # Delete all items from the users list
    cur.execute("DELETE FROM list WHERE user_id = ?", (session["user_id"],))
    con.commit()

    return redirect(f"/list/{session['user_id']}")


@app.route("/addingredients/<recipe_id>")
def addingredients(recipe_id):
 
    # Get ingredients from recipe
    ingredients = get_recipe_info(recipe_id)[1]

    # Add the ingredients to shopping list
    for item in ingredients:
        cur.execute("INSERT INTO list (user_id, item, quantity, units) VALUES (?, ?, ?, ?)", (session["user_id"], item["ingredient"], item["quantity"], item["units"]))
        con.commit()

    return redirect(f"/list/{session['user_id']}")


@app.route("/editrecipe/<user_id>/<recipe_id>", methods=["GET", "POST"])
@login_required
@user_specific
def editrecipe(user_id, recipe_id):

    if request.method == "POST":

        # Delete ingredients and steps to re-enter
        cur.execute("DELETE FROM ingredients WHERE recipe_id = ?", (recipe_id,))
        cur.execute("DELETE FROM steps WHERE recipe_id = ?", (recipe_id,))
        con.commit()

        # Get recipe title, description and servings and save to database
        title = request.form.get("title")

        if request.form.get("description") is not None:
            description = request.form.get("description")
        else:
            description = None

        if request.form.get("servings") is not None:
            servings = request.form.get("servings")
        else:
            servings = None

        # Update recipes table
        cur.execute("UPDATE recipes SET title=?, description=?, servings=? WHERE id = ? ", (title, description, servings, recipe_id))
        con.commit()

        ingredient_count = 0

        # Loop through each ingredient in the request
        for ingredient in request.form.getlist("ingredient"):
            
            # Get the quantity and units for ingredient
            quantity = request.form.getlist("quantity")[ingredient_count]
            units = request.form.getlist("units")[ingredient_count]

            # Add ingredient into database
            cur.execute("INSERT INTO ingredients (recipe_id, ingredient, quantity, units) VALUES (?, ?, ?, ?)", (recipe_id, ingredient, quantity, units))
            con.commit()

            ingredient_count += 1

        step_count = 0

        # Loop through each step in the request
        for step in request.form.getlist("step"):
            
            # Add step into database
            cur.execute("INSERT INTO steps (recipe_id, step) VALUES (?, ?)", (recipe_id, step))
            con.commit()

            step_count += 1

        return redirect(f"/recipe/{session['user_id']}/{recipe_id}")

    # If GET request
    else:
        # Get recipe info from database
        recipe, ingredients, steps, pictures = get_recipe_info(recipe_id)

        return render_template("editrecipe.html", recipe=recipe, ingredients=ingredients, steps=steps, pictures=pictures)


@app.route("/recipe/<user_id>/<recipe_id>")
@login_required
@user_specific
def recipe(user_id, recipe_id):
    recipe, ingredients, steps, picture = get_recipe_info(recipe_id)
    return render_template("recipe.html", recipe=recipe, ingredients=ingredients, steps=steps, picture=picture)


@app.route("/recipes/<user_id>")
@login_required
@user_specific
def recipes(user_id):
    recipes = cur.execute("SELECT * FROM recipes WHERE user_id = ?", (session['user_id'],)).fetchall()
    
    # Get the picture for each recipe
    picture_paths = []
    for recipe in recipes:
        picture = cur.execute("SELECT filename FROM pictures WHERE recipe_id = ?", (recipe['id'],)).fetchone()
        
        # If there is no picture, assign the default
        if picture == None:
            path = "/static/images/recipe-card-default.png"
        else:
            path = f"/static/uploads/{picture['filename']}"

        picture_paths.append(path)
    return render_template("recipes.html", recipes=recipes, pictures=picture_paths)


@app.route("/addrecipe", methods=["GET", "POST"])
@login_required
def addrecipe():

    if request.method == "POST":

        # Get recipe title, description and servings and save to database
        title = request.form.get("title")

        if request.form.get("description") is not None:
            description = request.form.get("description")
        else:
            description = None

        if request.form.get("servings") is not None:
            servings = request.form.get("servings")
        else:
            servings = None

        cur.execute("INSERT INTO recipes (user_id, title, description, servings) VALUES (?, ?, ?, ?)", (session['user_id'], title, description, servings))
        con.commit()

        # save the recipe id for use in ingredients and steps tables
        recipe_id = cur.lastrowid

        ingredient_count = 0

        # Loop through each ingredient in the request
        for ingredient in request.form.getlist("ingredient"):
            
            # Get the quantity and units for ingredient
            quantity = request.form.getlist("quantity")[ingredient_count]
            units = request.form.getlist("units")[ingredient_count]

            # Add ingredient into database
            cur.execute("INSERT INTO ingredients (recipe_id, ingredient, quantity, units) VALUES (?, ?, ?, ?)", (recipe_id, ingredient, quantity, units))
            con.commit()

            ingredient_count += 1

        step_count = 0

        # Loop through each step in the request
        for step in request.form.getlist("step"):
            
            # Add step into database
            cur.execute("INSERT INTO steps (recipe_id, step) VALUES (?, ?)", (recipe_id, step))
            con.commit()

            step_count += 1

        # Get picture from the request
        picture = request.files.get("picture")

        # Save picture to the upload folder
        filename = f"{uuid4().__str__()}-{secure_filename(picture.filename)}"
        picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Add picture info to database
        cur.execute("INSERT INTO pictures (recipe_id, filename) VALUES (?, ?)", (recipe_id, filename))
        con.commit()

        return redirect(f"/recipes/{session['user_id']}")
    
    else:
        return render_template("addrecipe.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    # Post request
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        result = cur.execute("SELECT * FROM users WHERE username= ?", (username,)).fetchone()

        if result is not None:
            # Check password is correct
            if check_password_hash(result["password"], password):    
                # Log user in
                session["username"] = result["username"]

                # Get user id
                id = result["id"]
                session["user_id"] = str(id)

                return redirect("/")
        
        # If login fails, reload page with errors
        return render_template("login.html", error="invalid_credentials")

    # Get request
    else:
        return render_template("login.html")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    # remove the username from the session
    session.pop("username", None)
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        # Check username is not taken
        result = cur.execute("SELECT 1 FROM users WHERE username = ?", (username,)).fetchone()

        if result is not None:
            # Reload page with username exists error
            return render_template("register.html", error="username_exists")
        
        # Check passwords match
        elif password != confirm:
            # Reload form with password match error
            return render_template("register.html", username=username, error="password_match") 
        
        else:
            # Create new user
            cur.execute("INSERT INTO users (username, password) VALUES (? ,?)", (username, generate_password_hash(password, method="scrypt")))
            con.commit()

            # Sign user in
            session['username'] = username
            id = cur.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
            session["user_id"] = str(id)

            return redirect("/")     

    else:
        return render_template("register.html")


if __name__ == '__main__':
    app.run()