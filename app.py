import os
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/get_username")
def get_username():
    details = mongo.db.users.find()
    return render_template("profile.html", details = details)

if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port = int(os.environ.get("PORT")), debug = True)