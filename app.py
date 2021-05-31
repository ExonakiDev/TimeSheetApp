from flask import Flask, flash, redirect, render_template, request, session
from flaskext.mysql import MySQL
from database import Database
import pymysql

# init flask app
app = Flask(__name__)
app.config['TESTING'] = False
# session secret key
app.secret_key = b'L\xdb\x1b\xc2\xa9\xbc\xc0\x84\xcb\xb67\x0c\xdf#hW'
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# init MySQL database
mysql = MySQL()
mysql.init_app(app)

# make cursor to db
# cursor = mysql.get_db().cursor()

@app.route("/")
def index():
    ## Placeholder
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    session.clear()
    # If user reached route via post method
    if request.method == "POST":
        if not request.form.get("username"):
            # Return error message TODO
            error = "Please enter username!"
            return render_template('login.html', error=error)
        elif not request.form.get("password"):
            # Return error message TODO
            error = "Please enter password!"
            return render_template('login.html', error=error)
        # TODO Check login


        # redirect to main page
        return redirect("/")
    # User reached route via get method
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    # session.pop('username', None)
    session.clear()
    # redirect to main page
    return redirect("/")

@app.route("/register")
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            # Return error message TODO
            return error
        elif not request.form.get("password"):
            # Return error message TODO
            return error
    else:
        return render_template("register.html")
