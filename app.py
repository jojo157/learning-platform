import os
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
    make_response,
    jsonify,
)
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


@app.errorhandler(404)
def page_not_found(e):
    """
    Routes user to 404 page when page not found.
    """
    return render_template("404.html"), 404


@app.route("/")
def index():
    """
    Renders the landing page for user to login or register.
    """
    return render_template("index.html")


# credit to below for before request function
# https://stackoverflow.com/questions/32237379/python-flask-redirect-to-https-from-http
@app.before_request
def before_request():
    """
    Force user to HTTPS connections
    """
    scheme = request.headers.get("X-Forwarded-Proto")
    if scheme and scheme == "http" and request.url.startswith("http://"):
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)


@app.route("/home")
def home():
    """
    Renders Home library page if user logged in with
    contents shown in date order fo creation.
    If user is not logged in, they are rendered to
    app landing page to register or login
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        site_contents = mongo.db.content.find({"view": "public"}).sort(
            "date_time", -1
        )
        level = mongo.db.users.find_one({"username": session["user"]})[
            "access_level"
        ]
        query = " "

    return render_template(
        "home.html", site_contents=site_contents, level=level, query=query
    )


@app.route("/home/score_up/", methods=["GET", "POST"])
def score_up():
    """
    Increases the clicked articles up vote score by 1
    when called by a logged in user.
    If not logged in, renders app landing page
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        req = request.get_json()
        rated_article = req["article"]
        document = mongo.db.content.find_one({"_id": ObjectId(rated_article)})
        current_score = document["rating_up"]
        new_score = current_score + 1
        mongo.db.content.update_one(
            {"_id": ObjectId(rated_article)},
            {"$set": {"rating_up": new_score}},
        )
        res = make_response("score changed")

    return res


@app.route("/home/score_down/", methods=["GET", "POST"])
def score_down():
    """
    Increases the clicked articles down vote score by 1
    when called by a logged-in user.
    If not logged in, renders app landing page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        req = request.get_json()
        rated_article = req["article"]
        document = mongo.db.content.find_one({"_id": ObjectId(rated_article)})
        current_score = document["rating_down"]
        new_score = current_score + 1
        mongo.db.content.update_one(
            {"_id": ObjectId(rated_article)},
            {"$set": {"rating_down": new_score}},
        )
        res = make_response("score changed")

    return res


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Returns search results from user input and
    renders the library page with relevant content.
    If not logged in, renders app landing page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        query = request.form.get("search")
        content = mongo.db.content.find({"$text": {"$search": query}})
        level = session.get("access")

    return render_template(
        "home.html", site_contents=content, level=level, query=query
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers a user if the choosen username doesnt already exist.
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists, try another username", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email").lower(),
            "access_level": "general",
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        session["access"] = "general"
        flash("Registration Successful!", "success")
        return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    The entered details are checked against the users collection
    and if a match is found, the user is logged in.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
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
    """
    A user is logged out and the session data is removed.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        flash("You have been logged out", "success")
        session.pop("user")
        session.pop("access")

    return redirect(url_for("login"))


@app.route("/profile")
def profile():
    """
    Renders the users profile page with thier specific data
    If user is not logged in, then returned to landing page.
    """
    if not session.get("user") is None:
        name = mongo.db.users.find_one({"username": session["user"]})[
            "first_name"
        ]
        notes = mongo.db.posts.find({"username": session["user"]}).sort(
            "date_time", -1
        )
        favourites = mongo.db.favourites.find({"username": session["user"]})
        return render_template(
            "profile.html", name=name, notes=notes, favourites=favourites
        )

    return render_template("index.html")


@app.route("/search_fav/<string:query>", methods=["GET", "POST"])
def search_fav(query):
    """
    Renders the library page with data related
    to the clicked favourite article.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        content = mongo.db.content.find({"$text": {"$search": query}})

    return render_template("home.html", site_contents=content, query=query)


@app.route("/notes", methods=["GET", "POST"])
def notes():
    """
    Creates a new sticky note on the users profile with data entered.
    The created date is added in the function call.
    If a user is not logged in, tpage rendered is landing page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        if request.method == "GET":
            return render_template("notes.html")

        if request.method == "POST":
            newpost = {
                "username": session.get("user").lower(),
                "title": request.form.get("title"),
                "note": request.form.get("body"),
                "date": datetime.now().strftime("%d-%m-%Y"),
                "date_time": datetime.now(),
            }
            mongo.db.posts.insert_one(newpost)

            # put the new user into 'session' cookie
            flash("Note added!", "success")
        return redirect(url_for("profile"))


@app.route("/editnote/<string:note_id>", methods=["GET", "POST"])
def editnote(note_id):
    """
    Allows user to edit the sticky note they selected.
    Once updated a success message is given on users profile.
    If not logged in, renders landing page.
    Added condition to ensure a user can only edit their notes. 
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:

        if request.method == "GET":
            note_data = mongo.db.posts.find_one({"_id": ObjectId(note_id)})
            if session.get("user") == note_data["username"]:
                return render_template("editnote.html", note=note_data)
            else:
                return redirect(url_for("profile"))

        if request.method == "POST":
            note_data = mongo.db.posts.find_one({"_id": ObjectId(note_id)})
            if session.get("user") == note_data["username"]:
                updated_post = {
                    "username": session.get("user").lower(),
                    "title": request.form.get("title"),
                    "note": request.form.get("body"),
                }
                mongo.db.posts.update_one(
                    {"_id": ObjectId(note_id)}, {"$set": updated_post}
                )

                flash("Note updated!", "success")
                return redirect(url_for("profile"))
            else:
                return redirect(url_for("profile"))



@app.route("/delete_note/<string:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    """
    Allows user to delete the sticky note they selected.
    Once deleted a success message is given on users profile.
    If not logged in, renders landing page.
    User can only delete their sticky notes.
    """
    if request.method == "GET":
        if not session.get("user") is None:
            note_data = mongo.db.posts.find_one({"_id": ObjectId(note_id)})
            if session.get("user") == note_data["username"]:
                mongo.db.posts.remove({"_id": ObjectId(note_id)})
                flash("Note has been Deleted", "success")
        return redirect(url_for("profile"))
    return redirect(url_for("index"))


@app.route("/content", methods=["GET", "POST"])
def content():
    """
    Allows an admin user to add an article to the library page.
    The data is taken from the form and
    stored in the Mongo DB content collection.
    Success messgae given to user and redirected to library.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:

        if request.method == "GET":
            if session.get("access") == "admin":
                return render_template("content.html")

        if request.method == "POST":
            newpost = {
                "user": session.get("user").lower(),
                "category": request.form.get("category"),
                "title": request.form.get("title"),
                "content": request.form.get("body"),
                "date": datetime.now().strftime("%d-%m-%Y"),
                "keywords": request.form.get("keywords"),
                "view": "public",
                "rating_up": 0,
                "rating_down": 0,
                "picture": request.form.get("picture"),
                "resource": request.form.get("resource"),
                "date_time": datetime.now(),
            }
            mongo.db.content.insert_one(newpost)

            flash("Post added!", "success")
            return redirect(url_for("home"))


@app.route("/editcontent/<string:content_id>", methods=["GET", "POST"])
def editcontent(content_id):
    """
    Allows admin user to edit selected article and
    updates the revelent document in the collection content.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        if request.method == "GET":
            if session.get("access") == "admin":
                post_data = mongo.db.content.find_one(
                    {"_id": ObjectId(content_id)}
                )
                return render_template("editcontent.html", post=post_data)

        if request.method == "POST":
            updated_content = {
                "category": request.form.get("category"),
                "title": request.form.get("title"),
                "content": request.form.get("body"),
                "keywords": request.form.get("keywords"),
                "picture": request.form.get("picture"),
                "resource": request.form.get("resource"),
            }
            mongo.db.content.update_one(
                {"_id": ObjectId(content_id)}, {"$set": updated_content}
            )

            flash("Post updated!", "success")
            return redirect(url_for("home"))


@app.route("/delete_content/<string:content_id>", methods=["GET", "POST"])
def delete_content(content_id):
    """
    Allows admin user to delete the selected article.
    A success message is given and user redirected to library apge.
    """
    if request.method == "GET":
        if not session.get("user") is None:
            if session.get("access") == "admin":
                mongo.db.content.remove({"_id": ObjectId(content_id)})
                flash("Post has been Deleted", "success")
            return redirect(url_for("home"))
    return redirect(url_for("profile"))


@app.route("/fav_content/", methods=["GET", "POST"])
def fav_content():
    """
    Allows a user to add an article as a favourite to their profile,
    if not previously favoured.
    If not logged in, user is returned to landing page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        req = request.get_json()
        content_id = req["article"]
        # check if favoured article before
        existing_fav = mongo.db.favourites.find_one(
            {"content_id": ObjectId(content_id)}
        )
        if not existing_fav:
            # add favourite to collection as hasn't been added before
            content_title = mongo.db.content.find_one(
                {"_id": ObjectId(content_id)}
            )["title"]
            favour = {
                "content_id": ObjectId(content_id),
                "username": session["user"],
                "content_title": content_title,
            }
            mongo.db.favourites.insert_one(favour)
        res = make_response("favoured")
        return res


@app.route("/delete_fav/<string:fav_title>", methods=["GET", "POST"])
def delete_fav(fav_title):
    """
    Allows user to remove a favourite shortlin from their profile.
    If not logged in, user is returned to landing page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        if request.method == "GET":
            mongo.db.favourites.remove({"content_title": fav_title})
            flash("Favourite has been Deleted", "success")
        return redirect(url_for("profile"))


@app.route("/user_settings", methods=["GET", "POST"])
def user_settings():
    """
    Allows a registered user to update their account settings.
    Success message displayed and rendered to profile page.
    If not logged in, user is returned to landing page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        if request.method == "GET":
            user_details = mongo.db.users.find_one(
                {"username": session["user"]}
            )
            return render_template(
                "usersettings.html", user_details=user_details
            )

        if request.method == "POST":
            user_details = mongo.db.users.find_one(
                {"username": session["user"]}
            )
            if request.form.get("password") == "Pf########1!":
                updated = {
                    "first_name": request.form.get("first_name"),
                    "last_name": request.form.get("last_name"),
                    "email": request.form.get("email").lower(),
                    "access_level": user_details["access_level"],
                    "password": user_details["password"],
                }
                mongo.db.users.update_one(
                    {"username": session["user"]}, {"$set": updated}
                )

            else:
                updated = {
                    "password": generate_password_hash(
                        request.form.get("password")
                    ),
                    "first_name": request.form.get("first_name"),
                    "last_name": request.form.get("last_name"),
                    "email": request.form.get("email"),
                    "access_level": user_details["access_level"],
                }
                mongo.db.users.update_one(
                    {"username": session["user"]}, {"$set": updated}
                )
            flash("Profile Updated", "success")
        return render_template("profile.html")


@app.route("/admin")
def admin():
    """
    Renders admin page with details of all registered users,
    to an admin user only.
    If not admin, renders your profile page.
    """
    if session.get("user") is None:
        return render_template("index.html")

    else:
        user_details = mongo.db.users.find_one({"username": session["user"]})
        if user_details["access_level"] == "admin":
            all_users = mongo.db.users.find().sort("first_name", 1)
            return render_template("admin.html", all_users=all_users)

    return redirect(url_for("profile"))


@app.route("/admin_edit/<string:user_to_edit>", methods=["GET", "POST"])
def admin_edit(user_to_edit):
    """
    Allows admin user to edit selected users details.
    If not admin, renders your profile.
    """
    if session.get("access") == "admin":
        # check admin access level
        if request.method == "GET":
            user_data = mongo.db.users.find_one({"username": user_to_edit})
            return render_template("adminedit.html", user_data=user_data)

        if request.method == "POST":
            user_details = mongo.db.users.find_one({"username": user_to_edit})

            if request.form.get("password") == "Pf########1!":
                updated = {
                    "first_name": request.form.get("first_name"),
                    "last_name": request.form.get("last_name"),
                    "email": request.form.get("email"),
                    "access_level": request.form.get("access_level").lower(),
                    "password": user_details["password"]
                }
                mongo.db.users.update_one(
                    {"username": user_to_edit}, {"$set": updated}
                )

            else:
                updated = {
                    "password": generate_password_hash(
                        request.form.get("password")
                    ),
                    "first_name": request.form.get("first_name"),
                    "last_name": request.form.get("last_name"),
                    "email": request.form.get("email").lower(),
                    "access_level": request.form.get("access_level").lower(),
                }
                mongo.db.users.update_one(
                    {"username": user_to_edit}, {"$set": updated}
                )

            flash("User has been Updated", "success")

        return redirect(url_for("admin"))

    return redirect(url_for("profile"))


@app.route("/admin_delete/<string:user_to_delete>", methods=["GET", "POST"])
def admin_delete(user_to_delete):
    """
    Allows admin user to delete selected user.
    If not admin, renders your profile.
    """
    if not session.get("user") is None:

        if session.get("access") == "admin":
            # check admin access level

            if request.method == "GET":
                mongo.db.users.remove({"username": user_to_delete})
                mongo.db.favourites.remove({"username": user_to_delete})
                mongo.db.posts.remove({"username": user_to_delete})
                flash("User has been Deleted", "success")
            return redirect(url_for("admin"))

        return redirect(url_for("profile"))

    return redirect(url_for("profile"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Renders contact form to allow all to fill in.
    Once form submitted, email sent using gmail and Flask mail to admin.
    User presented with message and return to contact page.
    """
    if request.method == "GET":
        return render_template("contact.html")

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
            body=f"Name: {name} \nUsername: {username} \n"
            f"Email: {email} \nMessage: {message}",
            sender=email,
            recipients=[os.environ.get("MAIL_USERNAME")],
        )
        mail.send(msg)
        flash("Message sent, an admin will contact you shortly", "success")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True
    )
