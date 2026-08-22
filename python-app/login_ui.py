import tkinter as tk
from tkinter import messagebox
from login_logic import authenticate_user

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Form')
        self.root.geometry('300x180')
        self.root.resizable(False, False)

        # Username label and entry
        self.lbl_username = tk.Label(root, text='Username:')
        self.lbl_username.pack(pady=(20, 5))
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        # Password label and entry
        self.lbl_password = tk.Label(root, text='Password:')
        self.lbl_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show='*')
        self.entry_password.pack(pady=5)

        # Login button
        self.btn_login = tk.Button(root, text='Login', command=self.login)
        self.btn_login.pack(pady=(10, 10))

        # Bind Return key to login button
        root.bind('<Return>', self.login)

    def login(self, event=None):
        username = self.entry_username.get().strip()
        password = self.entry_password.get()

        success, message = authenticate_user(username, password)
        if success:
            messagebox.showinfo('Success', message)
            self.clear_entries()
        else:
            messagebox.showerror('Error', message)

    def clear_entries(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = LoginUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
