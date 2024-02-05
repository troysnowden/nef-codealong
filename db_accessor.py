usersData = {
    "student1": {
        "name": "John Doe",
        "password": "password1",
        "is_student": True,
        "num_rewards": 0
    }, 
    "student2": {
        "name": "Jane Doe",
        "password": "password2",
        "is_student": True,
        "num_rewards": 1
    }, 
    "admin3": {
        "name": "Admin Doe",
        "password": "password3",
        "is_student": False
    }
}

def increment_student_rewards(username):
    usersData[username]["num_rewards"] += 1

def push_user_to_db(username, password):
    # not yet implemented

    return True

# def is_user_registered(username, password):
#     registered_users = get_registered_users()

#     user = registered_users.get(username)

#     if user and user.get("password") == password:
#         return True
#     else:
#         return False


def get_registered_users():
    #key = username, value = password
    return usersData