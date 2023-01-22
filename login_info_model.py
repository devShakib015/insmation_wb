class LoginInfo():
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
