class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False

    def __repr__(self):
        return f"User(username='{self.username}', password='{self.password}')"
    
    def check_password(self, password):
        if self.password == password:
            self.is_authenticated = True
            return True
        else:
            self.is_authenticated = False
            return False
    
    def is_authenticated(self):
        return self.is_authenticated
