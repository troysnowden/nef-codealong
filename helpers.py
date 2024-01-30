#notes
# original logic to be:
# - password length must be at least 5 characters (extreme/boundary testing)
# - password must contain a special char (@, ! or $)
# - passwords must match

# talk about:
# - magic numbers
# - good variable/method names
# - code duplication

from db_accessor import push_user_to_db, get_registered_users


def register_user(username, password, confirmed_password):

    if check(password):
        return push_user_to_db(username, password)
    else:
        return False

def check(password):
    if len(password) < 5:
        return False
    
    containsSpecialChar = False

    if password[0] == '!' or password[0] == '@':
        containsSpecialChar = True
    
    if password[1] == '!' or password[1] == '@':
        containsSpecialChar = True
    
    if password[2] == '!' or password[2] == '@':
        containsSpecialChar = True
    
    if password[3] == '!' or password[3] == '@':
        containsSpecialChar = True
    
    if password[4] == '!' or password[4] == '@':
        containsSpecialChar = True
    
    return containsSpecialChar


def login_user(username, password):
    registered_users = get_registered_users()
    
    if registered_users.get(username) == password:
        return True
    else:
        return False


def is_admin(username):
    return username == "admin2"