from user_controller import UserController, User
import tkinter as tk

class Application(tk.Frame):
    controller = UserController()
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets_login()
        # self.show_users()

    def validate_password(self, password, label):
        try:
            int(password) and len(password) == 4
            label.config(text='')
        except:
            label.config(text='Please, enter a valid password!')

    def check_credentials_login(self, username, password, username_label, password_label):
        self.validate_password(password, password_label)
        user_exists = self.controller.find_user_by_username(username)
        if user_exists:
            if user_exists.password == password:
                self.show_users()
            else:
                password_label.config(text='Incorrect username and/or password!')
        else:
            username_label.config(text='User does not exist!')

    def create_widgets_login(self):
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

        login_button = tk.Button(self, text='Login', command=self.check_credentials_login(username_input.get(), password_input.get(), username_answer_label, password_answer_label))
        login_button.grid(row=7, column=1)

    def show_users(self):
        title_label = tk.Label(self, text='Users')
        title_label.grid(row=0, column=3)

        headers = ['username', 'name', 'password', 'role']
        for i in range(len(headers)):
            self.e = tk.Entry(self, width=20, fg='black', font=('Arial', 16, 'bold'))
            self.e.grid(row=1, column=i)
            self.e.insert(tk.END, headers[i])
        
        list_users = list(map(lambda u: User(u), self.controller.get_users() or []))
        # users = [list(col) for col in zip(*[u.to_list() for u in self.controller.get_users()])]
        for i in range(len(list_users)):
            for j in range(len(headers)):
                self.e = tk.Entry(self, width=20, fg='blue', font=('Arial', 16, 'bold'))
                self.e.grid(row=i + 2, column=j)
                self.e.insert(tk.END, list_users[i][headers[j]])
            self.edit_button = tk.Button(self, text='Edit')
            self.e = tk.Entry(self, width=20, fg='black', font=('Arial', 16, 'bold'))
            self.e.grid(row=i, column=4)
            self.e.insert(tk.END, self.edit_button)

    def create_user_c(self):
        controller.create()

    def create_user(self):
        title_label = tk.Label(text='Add new user')
        title_label.grid(row=0, column=1)

        username_label = tk.Label(self, text='Username')
        username_label.config(row=1, column=0)
        username_input = tk.Entry(self)
        username_input.config(row=1, column=1)
        
        name_label = tk.Label(self, text='Name')
        name_label.config(row=3, column=0)
        name_input = tk.Entry(self)
        name_input.config(row=3, column=1)
        
        password_label = tk.Label(self, text='Password')
        password_label.config(row=5, column=0)
        password_input = tk.Entry(self)
        password_input.config(row=5, column=1)
        
        role_label = tk.Label(self, text='Role')
        role_label.config(row=7, column=0)
        role_input = tk.Entry(self)
        role_input.config(row=7, column=1)

        answer_label = tk.Label(self, text='', fg='red')
        answer_label.grid(row=9, column=1)
        add_button = tk.Button(self, text='Add', command=create_user_c)
        add_button.grid(row=10, column=1)

    def update_user_c(self):
        controller.update()

    def delete_user_c(self):
        controller.delete()

    def update_user(self):
        title_label = tk.Label(text='Update user')
        title_label.grid(row=0, column=2)

        username_label = tk.Label(self, text='Username')
        username_label.config(row=1, column=0)
        username_input = tk.Entry(self)
        username_input.config(row=1, column=1)
        
        name_label = tk.Label(self, text='Name')
        name_label.config(row=3, column=0)
        name_input = tk.Entry(self)
        name_input.config(row=3, column=1)
        
        password_label = tk.Label(self, text='Password')
        password_label.config(row=5, column=0)
        password_input = tk.Entry(self)
        password_input.config(row=5, column=1)
        
        role_label = tk.Label(self, text='Role')
        role_label.config(row=7, column=0)
        role_input = tk.Entry(self)
        role_input.config(row=7, column=1)

        answer_label = tk.Label(self, text='', fg='red')
        answer_label.grid(row=9, column=1)
        update_button = tk.Button(self, text='Update', command=update_user_c)
        update_button.grid(row=10, column=1)
        delete_button = tk.Button(self, text='Delete', command=delete_user_c)
        delete_button.grid(row=10, column=3)

    def open_users_window(self):
        # Toplevel object which will
        # be treated as a new window
        newWindow = tk.Toplevel(self.master)
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
        # sets the geometry of toplevel
        newWindow.geometry("200x200")
    
        # A Label widget to show in toplevel
        tk.Label(newWindow, text ="This is a new window").pack()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('CRUD usuarios')
    app = Application(master=root)
    app.mainloop()
