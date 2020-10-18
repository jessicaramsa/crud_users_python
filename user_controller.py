from user import User
import json
import hashlib

class UserController:
    def hash_password(self, password):
        return hashlib.md5(bytes(password)).hexdigest()

    def get_users(self):
        with open('users.json', encoding='utf-8') as users_file:
            return list(map(lambda u: User(**u), json.load(users_file) or []))

    def find_user_by_username(self, username):
        users = self.get_users()
        user = list(filter(lambda u: u.username.lower() in username, users))
        return user.pop() if user else None

    def find_user_by_password(self, password):
        # password = hashlib.md5(bytes(password)).hexdigest()
        users = self.get_users()
        user = list(filter(lambda u: u.password in password, users))
        return user.pop() if user else None

    def create(self, user):
        if self.find_user_by_username(user.username):
            raise TypeError('User already exists!')

        users = self.get_users()
        user.password = self.hash_password(user.password)
        users.append(user)
        if not save_users(users):
            raise TypeError('Something went wrong!')
        return 'User created succesfully!'
    
    def update(self, user):
        if not self.find_user_by_username(user.username):
            raise TypeError('This user does not exist!')
        
        users = self.get_users()
        index_user_to_update = users.index(user)
        users.insert(index_user_to_update, user)
        if not self.save_users(users):
            raise TypeError('Something went wrong!')

    def delete(self, user):
        users = get_users(self)
        user_to_delete = self.find_user_by_username(user.username)
        users.remove(user_to_delete)
        if not self.save_users(users):
            raise TypeError('Something went wrong!')

    def save_users(self, users):
        try:
            with open('users.json', 'w', encoding='utf-8') as users_file:
                json.dump(users, users_file, indent=4)
                return True
        except:
            return False
