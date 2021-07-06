import os
from flask import Flask, flash, render_template, redirect, request, session, url_for, Response, make_response
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from datetime import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")


mongo = PyMongo(app)
mail = Mail(app)
  
@app.route("/")
def index():
    return render_template("index.html")


@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


@app.route("/home")
def home():
    if not session.get("user") is None:
        site_contents = mongo.db.content.find( {"view" : "public"}).sort("date", -1)
        level = mongo.db.users.find_one( {"username" : session["user"]})["access_level"]
        return render_template("home.html", site_contents = site_contents, level = level)
    return render_template("index.html")


@app.route("/home/score_up/<string:rated_article>")
def score_up(rated_article):
    document = mongo.db.content.find_one({"_id": ObjectId(rated_article)})
    current_score = document["rating_up"]
    new_score = current_score + 1
    mongo.db.content.update_one({"_id": ObjectId(rated_article)}, { "$set": {"rating_up": new_score} })
    return redirect(url_for("home"))
    


@app.route("/home/score_down/<string:rated_article>")
def score_down(rated_article):  
    document = mongo.db.content.find_one({"_id": ObjectId(rated_article)})
    current_score = document["rating_down"]
    new_score = current_score + 1
    mongo.db.content.update_one({"_id": ObjectId(rated_article)}, { "$set": {"rating_down": new_score} })
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search")
    content = mongo.db.content.find({"$text": {"$search": query}})
    return render_template("home.html", site_contents = content)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, try another username", "error")
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
        flash("Registration Successful!", "success")
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
                        session["access"] = existing_user["access_level"]
                        return redirect(url_for("home"))
                            
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out", "success")
    session.pop("user")
    session.pop("access")
    return redirect(url_for("login"))





@app.route("/profile")
def profile():
    if not session.get("user") is None:
        name = mongo.db.users.find_one({"username": session["user"]})["first_name"]
        notes = mongo.db.posts.find({"username": session["user"]}).sort("date", -1)
        favourites = mongo.db.favourites.find({"username": session["user"]})
        return render_template("profile.html", name=name, notes=notes, favourites=favourites)
    return render_template("index.html")


@app.route("/search_fav/<string:query>", methods=["GET", "POST"])
def search_fav(query):
    content = mongo.db.content.find({"$text": {"$search": query}})
    return render_template("home.html", site_contents = content)


@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "GET":   
        if not session.get("user") is None:
            return render_template("notes.html")
        return redirect(url_for('profile'))
  
    if request.method == "POST":
            newpost = {
                "username": session.get("user").lower(),
                "title": request.form.get("title"),
                "note": request.form.get("body"),
                "date": datetime.now().strftime('%d-%m-%Y')
            }
            mongo.db.posts.insert_one(newpost)

            # put the new user into 'session' cookie
            flash("Note added!", "success")
            return redirect(url_for('profile'))
    return render_template("register.html")


@app.route("/editnote/<string:note_id>", methods=["GET", "POST"])
def editnote(note_id):
    if request.method == "GET":   
        if not session.get("user") is None:
            note_data = mongo.db.posts.find_one({"_id": ObjectId(note_id)})
            return render_template("editnote.html", note=note_data)
        return redirect(url_for('profile'))
  
    if request.method == "POST":
            updated_post = {
                "username": session.get("user").lower(),
                "title": request.form.get("title"),
                "note": request.form.get("body")
            }
            mongo.db.posts.update_one({"_id": ObjectId(note_id)}, { "$set": updated_post })

            flash("Note updated!", "success")
            return redirect(url_for('profile'))
    return render_template("register.html")


@app.route("/delete_note/<string:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    if request.method == "GET":
        if not session.get("user") is None:
            mongo.db.posts.remove({"_id": ObjectId(note_id)})
            flash("Note has been Deleted", "success")
        return redirect(url_for('profile'))
    return redirect(url_for('profile'))

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
            "date": datetime.now().strftime('%d-%m-%Y'),
            "keywords": request.form.get("keywords").lower(),
            "view": "public",
            "rating_up": 0,
            "rating_down":0,
            "picture": request.form.get("picture"),
            "resource": request.form.get("resource")
        }
        mongo.db.content.insert_one(newpost)

        flash("Post added!", "success")
        return redirect(url_for('home'))

    return render_template("register.html")


@app.route("/editcontent/<string:content_id>", methods=["GET", "POST"])
def editcontent(content_id):
    if request.method == "GET":   
        if not session.get("user") is None:
            post_data = mongo.db.content.find_one({"_id": ObjectId(content_id)})
            return render_template("editcontent.html", post=post_data)
        return redirect(url_for('home'))
  
    if request.method == "POST":
            updated_content = {
                "category": request.form.get("category"),
                "title": request.form.get("title"),
                "content": request.form.get("body"),
                "keywords": request.form.get("keywords").lower(),
                "picture": request.form.get("picture"),
                "resource": request.form.get("resource")
            }
            mongo.db.content.update_one({"_id": ObjectId(content_id)}, { "$set": updated_content })

            flash("Post updated!", "success")
            return redirect(url_for('home'))
    return render_template("register.html")


@app.route("/delete_content/<string:content_id>", methods=["GET", "POST"])
def delete_content(content_id):
    if request.method == "GET":
        if not session.get("user") is None:
            mongo.db.content.remove({"_id": ObjectId(content_id)})
            flash("Post has been Deleted", "success")
        return redirect(url_for('home'))
    return redirect(url_for('profile'))

@app.route("/fav_content/<string:content_id>")
def fav_content(content_id):
    if request.method == "GET":
        if not session.get("user") is None:
            #check if favoured article before
            existing_fav = mongo.db.favourites.find_one({"content_id": ObjectId(content_id)})
            if not existing_fav:
                #add favourite to collection as hasnt been added before
                content_title= mongo.db.content.find_one({"_id": ObjectId(content_id)})["title"]
                favour = {
                    "content_id": ObjectId(content_id),
                    "username": session["user"],
                    "content_title": content_title
                }
                mongo.db.favourites.insert_one(favour)  

            return redirect(url_for("home"))
        return render_template("register.html")


@app.route("/delete_fav/<string:fav_title>", methods=["GET", "POST"])
def delete_fav(fav_title):
    if request.method == "GET":
        if not session.get("user") is None:
            mongo.db.favourites.remove({"content_title": fav_title})
            flash("Favourite has been Deleted", "success")
        return redirect(url_for('profile'))
    return redirect(url_for('profile'))

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
            "password": user_details["password"],
            "access_level": user_details["access_level"]
           }
           mongo.db.tasks.update_one({"username": session["user"]}, { "$set": updated})
        else :
            updated = {
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "access_level": user_details["access_level"]
           }
            mongo.db.users.update_one({"username": session["user"]}, { "$set": updated})

        flash("Profile Updated", "success")
    return render_template("profile.html")


@app.route("/admin")
def admin():
    if not session.get("user") is None:
        user_details = mongo.db.users.find_one({"username": session["user"]})
        if user_details["access_level"] == "admin":
            all_users = mongo.db.users.find().sort("first_name", 1)
            return render_template("admin.html", all_users=all_users)
    return redirect(url_for('profile'))
        
@app.route("/admin_edit/<string:user_to_edit>", methods=["GET", "POST"])
def admin_edit(user_to_edit):
    if request.method == "GET":
        user_data = mongo.db.users.find_one({"username": user_to_edit})
        return render_template("adminedit.html", user_data=user_data)
    
    if request.method == "POST":
        user_details = mongo.db.users.find_one({"username": user_to_edit})
        if user_details["password"]== "######":
           updated = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": user_details["password"],
            "access_level": request.form.get("access_level").lower()
           }
           mongo.db.tasks.update_one({"username": user_to_edit}, { "$set": updated})
        else :
            updated = {
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "access_level": request.form.get("access_level").lower()
           }
            mongo.db.users.update_one({"username": user_to_edit}, { "$set": updated})
        
        flash("User has been Updated", "success")
    return redirect(url_for('admin'))


@app.route("/admin_delete/<string:user_to_delete>", methods=["GET", "POST"])
def admin_delete(user_to_delete):
    if not session.get("user") is None:
        if request.method == "GET":
            mongo.db.users.remove({"username": user_to_delete})
            mongo.db.favourites.remove({"username": user_to_delete})
            mongo.db.posts.remove({"username": user_to_delete})
            flash("User has been Deleted", "success")
        return redirect(url_for('admin'))
    return redirect(url_for('profile'))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html')

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        if not session.get("user") is None:
            username = session["user"]
        else:
            username = "guest"

        msg = Message(
            subject=f"Finance Mind message from {name}",
            body = f"Name: {name} \nUsername: {username} \nEmail: {email} \nMessage: {message}",
            sender = email,
            recipients=[os.environ.get("MAIL_USERNAME")]
        )

        mail.send(msg)
        flash("Message sent, an admin will contact you shortly", "success")
    return render_template("contact.html")
    
  


if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port = int(os.environ.get("PORT")), debug = True)