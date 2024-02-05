from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from helpers import register_user, login_user, is_student, add_student_reward, get_student_users, login_required, get_logged_in_user_data

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@login_required
def index():
    user_data = get_logged_in_user_data(session["username"])

    if not user_data["is_student"]:
        student_data = get_student_users()
    else:
        student_data = None

    return render_template('index.html', user_data=user_data, student_data=student_data)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirmation = request.form.get("confirmation")

        if register_user(username, password, password_confirmation):
            session["username"] = "username1" # currently a dummy value
            return redirect("/")
        else:
            return render_template('register.html', error_hit=True)

    else:
        return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if login_user(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template('login.html', error_hit=True)
    else:
        return render_template('login.html')

@app.route('/mybarcode')
def myaccount():
    return render_template('mybarcode.html')

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')   

@app.route('/add-reward', methods=["POST"])
@login_required
def add_reward():  
    username = request.form.get("username")
    print("Username: " + username)
    add_student_reward(username)

    return redirect('/')


@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def not_found():
    # replace with new 404 template
    return render_template('index.html')