import tkinter as tk
from tkinter import messagebox
import re
from auth import verify_login


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("300x180")
        self.root.resizable(False, False)

        # Username label and entry
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=(20, 0))
        self.entry_username = tk.Entry(root, width=30)
        self.entry_username.pack()

        # Password label and entry
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=(10, 0))
        self.entry_password = tk.Entry(root, width=30, show="*")
        self.entry_password.pack()

        # Login button
        self.btn_login = tk.Button(root, text="Login", width=10, command=self.handle_login)
        self.btn_login.pack(pady=(15, 0))

    def validate_input(self, username: str, password: str) -> bool:
        # Basic input validation
        if not username or not password:
            messagebox.showerror("Input Error", "Username and password cannot be empty.")
            return False
        # Validate username: alphanumeric, 3-20 chars
        if not re.fullmatch(r'[A-Za-z0-9]{3,20}', username):
            messagebox.showerror("Input Error", "Username must be 3-20 alphanumeric characters.")
            return False
        # Password minimal length
        if len(password) < 6:
            messagebox.showerror("Input Error", "Password must be at least 6 characters long.")
            return False
        return True

    def handle_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get()

        if not self.validate_input(username, password):
            return

        # Verify credentials
        if verify_login(username, password):
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.entry_password.delete(0, tk.END)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            self.entry_password.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
