import bcrypt
import json
import os
from user import User

filename='storage/users.json'

# user_manager.py
class UserManager:
    def __init__(self):
        self.users = self.load_users(filename)
    
    def load_users(self, filename):
        try:
            with open(filename, 'r') as file:
                users_data = json.load(file)
        except FileNotFoundError:
            users_data = []

        self.users = {}
        for user_data in users_data:
            self.users[user_data['username']] = User(user_data['username'], user_data['password'])

        return self.users
    
    def save_users(self, filename):
        try:
            with open(filename, 'r') as file:
                users_data = json.load(file)
        except FileNotFoundError:
            users_data = []

        for user in self.users.values():
            user_found = False
            for existing_user in users_data:
                if existing_user['username'] == user.username:
                    existing_user['password'] = user.password.decode('utf-8')
                    user_found = True
                    break

            if not user_found:
                users_data.append({
                    'username': user.username,
                    'password': user.password.decode('utf-8')
                })

        with open(filename, 'w') as file:
            json.dump(users_data, file, indent=4)
    def login_user(self, username, password):
        self.users = self.load_users(filename)  # Load users from the specified file

        if username not in self.users:
            print("User not found.")
            return False

        user = self.users[username]
        if user.check_password(password):
            print("Login successful!")
            return True
        else:
            print("Incorrect password.")
            return False
    
    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
        else:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            self.users[username] = User(username, hashed_password.decode('utf-8'))
            self.save_users(filename)
            print("Registration successful!")
            return True
