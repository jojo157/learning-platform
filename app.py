import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

  

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, try another username")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "access_level": "general"
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        session["access"] = "general"
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"], access=session["access"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        session["access"] = existing_user["access_level"]
                        return redirect(url_for(
                            "profile", username=session["user"], access=session["access"]) )
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    session.pop("access")
    return redirect(url_for("login"))





@app.route("/profile")
def profile():
    if not session.get("user") is None:
        name = mongo.db.users.find_one({"username": session["user"]})["first_name"]
        return render_template("profile.html", name=name)
    return render_template("index.html")

@app.route("/content", methods=["GET", "POST"])
def content():  
    if request.method == "GET":   
        if not session.get("user") is None:
            return render_template("content.html")
        return render_template("index.html")

    if request.method == "POST":
        newpost = {
            "user": session.get("user").lower(),
            "category": request.form.get("category").lower(),
            "title": request.form.get("title").lower(),
            "content": request.form.get("body"),
            "date": datetime.now(),
            "keywords": request.form.get("keywords").lower(),
            "view": "public",
            "rating_up": 0,
            "rating_down":0
        }
        mongo.db.content.insert_one(newpost)

        # put the new user into 'session' cookie
        flash("Post added!")
        return redirect(url_for("profile", username=session["user"], access=session["access"]))

    return render_template("register.html")

@app.route("/admin")
def admin():
    all_users = mongo.db.users.find()
    return render_template("admin.html", all_users=all_users)

@app.route("/user_settings", methods=["GET", "POST"])
def user_settings():
    if request.method == "GET":
        user_details = mongo.db.users.find_one({"username": session["user"]})
        return render_template("usersettings.html", user_details=user_details)


    if request.method == "POST":
        user_details = mongo.db.users.find_one({"username": session["user"]})
        if user_details["password"]== "######":
           updated = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": user_details.password,
            "access_level": user_details["access_level"]
           }
           mongo.db.tasks.update({"username": session["user"]}, update)
        else :
            updated = {
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "access_level": user_details["access_level"]
           }
            mongo.db.tasks.update_one({"username": session["user"]}, updated)
        flash("Profile Updated")
    return render_template("profile.html")

    





if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port = int(os.environ.get("PORT")), debug = True)