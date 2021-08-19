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
@myapp.route("/get_salons")
def get_salons():
    salons = mongo.db.salons.find()
    return render_template("salons.html", salons=salons)


@myapp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("This username already exists.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into a session cookie
        session['user'] = request.form.get("username").lower()
        flash("Registration successful")

    return render_template("register.html")


if __name__ == "__main__":
    myapp.run(host=os.environ.get('IP'),
              port=int(os.environ.get('PORT')), debug=True)
# remove this debug part after development
