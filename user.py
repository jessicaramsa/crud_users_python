import json

class User:
    username: str
    name: str
    password: int
    role: str

    def __init__(self, username, name, password, role):
        self.username = username
        self.name = name
        self.password = password
        self.role = role
    
    def __repr__(self):
        return {
            'username': self.username,
            'name': self.name,
            'password': self.password,
            'role': self.role
        }
    
    def __str__(self):
        return f'Username: {self.username}, Name: {self.name}, Password: {self.password}, Role: {self.role}'
