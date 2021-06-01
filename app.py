import sys
from flask import Flask, flash, redirect, render_template, request, url_for, session
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from flask_session import Session
from database import Database
import pymysql

# init flask app
app = Flask(__name__)
app.config['TESTING'] = False
# session secret key
app.secret_key = b'L\xdb\x1b\xc2\xa9\xbc\xc0\x84\xcb\xb67\x0c\xdf#hW'
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Password Hashing
bcrypt = Bcrypt(app)


# init MySQL database
mysql = MySQL()
mysql.init_app(app)

# make cursor to db
# cursor = mysql.get_db().cursor()

@app.route("/")
def index():
    ## Placeholder
    if not session.get("user_id"):
        return redirect("/login")
    return "Logged in"


@app.route("/login", methods=["GET", "POST"])
def login():
    """ User logs in here """
    error = None
    # Forget past user ids
    # session.clear()
    #Call DB class to init database
    db=Database()

    # If user reached route via post method
    if request.method == "POST":
        username = request.form.get("id")
        password = request.form.get("password")
        # print(username, password)
        if not username:
            # Return error message TODO
            error = "Please enter Employee ID!"
            # return render_template('login.html', error=error)
            flash("Please enter Employee ID!")
            return redirect(url_for("login"))
        elif not password:
            # Return error message TODO
            error = "Please enter password!"
            # return render_template('login.html', error=error)
            flash("Please enter password!")
            return redirect(url_for("login"))

        # Check login
        try:
            rows = db.check_credentials(username)
            print(rows, file=sys.stderr)
            if len(rows)!=1 or not (rows[0]["password"] == password):
                error = "Invalid credentials"
                flash("Invalid credentials")
                return redirect(url_for("login"))
            # Remember which user has logged in
            session["user_id"] = rows[0]["employee_id"]
        finally:
            # db.close_cursor()
            pass
        # redirect to main page
        flash('You were successfully logged in')
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


if __name__ == "__main__":
    app.run(debug=True)
