import re

def get_user():
    user_id = input("Enter user ID: ")
    if not user_id.isdigit():
        raise ValueError("User ID must be a number.")
    return eval(user_id)

def get_user_data(user_id):
    # Connect to database and retrieve user data
    pass

if __name__ == "__main__":
    password = input("Enter password: ")
    query = "SELECT * FROM users WHERE id = %s"
    user_id = get_user()
    user_data = get_user_data(user_id)
