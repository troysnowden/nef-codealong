from db_accessor import push_user_to_db, get_registered_users, increment_student_rewards
from flask import session, redirect
from functools import wraps


def register_user(username, password, confirmed_password):

    if check(password):
        return push_user_to_db(username, password, confirmed_password)
    else:
        return False

def login_user(username, password):
    user = get_registered_users().get(username)
    
    if user and user.get("password") == password:
        return True
    else:
        return False

def add_student_reward(username):
    user = get_registered_users().get(username)

    if user:
        return increment_student_rewards(username)
    else:
        return False

def get_logged_in_user_data(username):
    return get_registered_users().get(username)

def is_student(username):
    user = get_registered_users().get(username)
    return user and user.get("is_student")

def get_student_users():
    users = get_registered_users()
    student_users = {}

    for username, data in users.items():
        if data["is_student"]:
            student_users[username] = data
    
    return student_users

def check(password):
    minnumchar = 5
    if len(password) < minnumchar:
        return False
    
    containsSpecialChar = False

    for i in range(len(password)):
        if password[i] == '!' or password[i] == '@' or password[i] == '$':
            containsSpecialChar = True
            break
             
    passwordsmatch = False
    if password == confirmed_password:
        passwordsmatch = True
    
    return containsSpecialChar

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function