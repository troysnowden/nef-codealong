def push_user_to_db(username, password):
    # not yet implemented

    return true

def is_user_registered(username, password)
    registered_users = get_registered_users()
    
    if registered_users.get(username) == password:
        return True
    else:
        return False


def get_registered_users():
    #key = username, value = password
    return {
        "username1": "password1",
        "username2": "password2"
    }