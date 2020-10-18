from user_controller import UserController
from users_gui import UsersGUI
import tkinter as tk

class Application(tk.Frame):
    controller = UserController()
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def validate_password(self, password, label):
        try:
            int(password) and len(password) == 4
            label.config(text='')
        except:
            label.config(text='Please, enter a valid password!')

    def check_credentials(self, username, password, username_label, password_label):
        self.validate_password(password, password_label)
        user_exists = self.controller.find_user_by_username(username)
        if user_exists:
            if user_exists.password == password:
                user_gui = UsersGUI(self)
            else:
                password_label.config(text='Incorrect username and/or password!')
        else:
            username_label.config(text='User does not exist!')

    def create_widgets(self):
        title_label = tk.Label(self, text='Login')
        title_label.grid(row=0, column=1)

        username_label = tk.Label(self, text='Username')
        username_label.grid(row=1, column=0)
        username_input = tk.Entry(self)
        username_input.grid(row=1, column=1)
        username_answer_label = tk.Label(self, text='', fg='red')
        username_answer_label.grid(row=2, column=1)

        password_label = tk.Label(self, text='Password')
        password_label.grid(row=4, column=0)
        password_input = tk.Entry(self)
        password_input.grid(row=4, column=1)
        password_answer_label = tk.Label(self, text='', fg='red')
        password_answer_label.grid(row=5, column=1)

        login_button = tk.Button(self, text='Login', command=self.check_credentials(username_input.get(), password_input.get(), username_answer_label, password_answer_label))
        login_button.grid(row=7, column=1)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('CRUD usuarios')
    app = Application(master=root)
    app.mainloop()
