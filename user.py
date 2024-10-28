import bcrypt

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password.encode('utf-8')  # Codificar la contraseña hasheada a bytes
        self.is_authenticated = False

    def __repr__(self):
        return f"User(username='{self.username}', password='{self.password.decode('utf-8')}')"
    
    def check_password(self, password):

        if bcrypt.checkpw(password.encode('utf-8'), self.password):
            self.is_authenticated = True
            return True
        else:
            self.is_authenticated = False
            return False
    
    def is_authenticated(self):
        return self.is_authenticated
