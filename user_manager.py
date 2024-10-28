import bcrypt
import json
import os
from user import User

def load_users(filename=None):
    users = {}

    if filename is None or not os.path.exists(filename):
        return users

    try:
        with open(str(filename), 'r') as f:
            data = json.load(f)  # Load the JSON data
            if isinstance(data, list):  # Check if it's a list of user objects
                users = {user['username']: User(user['username'], user['password']) for user in data}
            else:  # Assume it's a single user object
                users = {
                    data['username']: User(
                        data['username'],
                        data['password'].encode('utf-8')  # Encode password as bytes
                    )
                }
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle file not found or invalid JSON
        pass

    return users

def save_users(users, filename='users.json'):
    users_data = []
    for user in users.values():
        users_data.append({
            'username': user.username,
            'password': user.password  # Decode password to string
        })
    # Provide a valid directory path for the filename
    directory = os.path.dirname(os.path.abspath(filename))
    os.makedirs(directory, exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(users_data, file, indent=4)

def login_user():
    users = load_users('users.json')

    username = input("Enter your username: ")
    if username not in users:
        print("User not found.")
        return False

    user = users[username]
    password = input("Enter your password: ")
    if user.check_password(password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False

def register_user():
    users = load_users('users.json')  # Provide the filename here

    username = input("Enter a username: ")
    if username in users:
        print("Username already exists.")
    else:
        password = input("Enter a password: ").encode('utf-8')  # Encode password as bytes
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        users[username] = User(username, hashed_password.decode('utf-8'))
        save_users(users)
        print("Registration successful!")
        return True
