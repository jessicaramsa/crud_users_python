import tkinter as tk

class UsersGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
    
    def create_widgets(self):
        pass

    def show_users(self):
        pass

    def create_user(self):
        pass

    def update_user(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    root.title('CRUD usuarios')
    root.geometry(400, 400)
    app = UsersGUI(master=root)
    app.mainloop()
