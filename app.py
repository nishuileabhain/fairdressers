import os
from flask import (Flask, redirect, flash,
                   render_template, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


myapp = Flask(__name__)

myapp.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
myapp.config["MONGO_URI"] = os.environ.get("MONGO_URI")
myapp.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(myapp)
# myapp refers to the object defined above


@myapp.route("/")
@myapp.route("/start")
def start():
    salons = list(mongo.db.salons.find())
    # wrapping find method into a python list to enable for loop
    return render_template("index.html", salons=salons)


@myapp.route("/get_salons")
def get_salons():
    salons = list(mongo.db.salons.find())
    # wrapping find method into a python list to enable for loop
    return render_template("salons.html", salons=salons)


@myapp.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    sal = list(mongo.db.salons.find({"$text": {"$search": query}}))
    return render_template("salons.html", salons=sal)


@myapp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # search db for username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        flash("new account created")

    return render_template("register.html")


@myapp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # hashed password matched with user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # actually a password issue
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@myapp.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        salons = list(mongo.db.salons.find())
        return render_template("profile.html", username=username,
                               salons=salons)

    return redirect(url_for("login"))


@myapp.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@myapp.route("/add_salon", methods=["GET", "POST"])
def add_salon():
    if request.method == "POST":
        # ternary operator so below line can be shorter
        warning = "on" if request.form.get("warning") else "off"
        # create a dictionary that can be passed via insert_one
        salon = {
            "category_name": request.form.get("category_name"),
            "company_name": request.form.get("company_name"),
            "contact_name": request.form.get("contact_name"),
            "description": request.form.get("description"),
            "warning": warning,
            "city": request.form.get("city"),
            "created_by": session["user"]
        }
        mongo.db.salons.insert_one(salon)
        flash("Review successfully added")
        return redirect(url_for("get_salons"))

    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template("add_salon.html", categories=categories)


@myapp.route("/edit_salon/<salon_id>", methods=["GET", "POST"])
def edit_salon(salon_id):
    # loads the review but editable
    if request.method == "POST":
        # ternary operator so below line can be shorter
        warning = "on" if request.form.get("warning") else "off"
        # create a dictionary that can be passed via insert_one
        changes = {
            "category_name": request.form.get("category_name"),
            "company_name": request.form.get("company_name"),
            "contact_name": request.form.get("contact_name"),
            "description": request.form.get("description"),
            "warning": warning,
            "city": request.form.get("city"),
            "created_by": session["user"],
            "date_created": request.form.get("date_created")
        }
        mongo.db.salons.update({"_id": ObjectId(salon_id)}, changes)
        flash("Review successfully changed")
        return redirect(url_for("get_salons"))

    salon = mongo.db.salons.find_one({"_id": ObjectId(salon_id)})
    return render_template("edit_salon.html",
                           salon=salon)


@myapp.route("/delete_salon/<salon_id>")
def delete_salon(salon_id):
    # nice to have confirmation
    mongo.db.salons.remove({"_id": ObjectId(salon_id)})
    flash("Review has been deleted")
    return redirect(url_for("get_salons"))


@myapp.route("/get_categories")
def get_categories():
    cats = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=cats)


@myapp.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # create a dictionary
        cat = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(cat)
        flash("new category added")
        # displays empty form if method is not post
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@myapp.route("/edit_category(<category_id>)", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
                    "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("category has been changed")
        return redirect(url_for("get_categories"))

    cat = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=cat)


@myapp.route("/delete_category(<category_id>)")
# actually using default method which is 'get'
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("category has been deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    myapp.run(host=os.environ.get('IP'),
              port=int(os.environ.get('PORT')), debug=True)
# remove this debug part after development
