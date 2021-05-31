from flask import Flask
from flaskext.mysql import MySQL

# init flask app
app = Flask(__name__)

# init MySQL database
mysql = MySQL()
mysql.init_app(app)

# make cursor to db
# cursor = mysql.get_db().cursor()

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
@login_required
def index():



@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    # If user reached route via post method
    if request.method == "POST":
        if not request.form.get("username"):
            # Return error message TODO
            return error
        elif not request.form.get("password"):
            # Return error message TODO
            return error

        # TODO Check login

        # redirect to main page
        return redirect("/")
    # User reached route via get method
    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    # redirect to main page
    return redirect("/")
