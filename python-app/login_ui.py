import tkinter as tk
from tkinter import messagebox
from login_logic import validate_login


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry('400x250')
        self.root.resizable(False, False)

        # Username or Email Label and Entry
        self.label_user = tk.Label(root, text="Username or Email:")
        self.label_user.pack(pady=(20, 5))

        self.entry_user = tk.Entry(root, width=40)
        self.entry_user.pack()

        # Password Label and Entry
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=(15, 5))

        self.entry_password = tk.Entry(root, width=40, show='*')
        self.entry_password.pack()

        # Buttons Frame
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=20)

        self.btn_login = tk.Button(self.frame_buttons, text="Login", width=12, command=self.login_user)
        self.btn_login.grid(row=0, column=0, padx=5)

        self.btn_clear = tk.Button(self.frame_buttons, text="Clear", width=12, command=self.clear_fields)
        self.btn_clear.grid(row=0, column=1, padx=5)

        # Message label
        self.label_message = tk.Label(root, text="", fg="red", font=('Arial', 10, 'bold'))
        self.label_message.pack(pady=5)

    def login_user(self):
        username_or_email = self.entry_user.get().strip()
        password = self.entry_password.get()

        # Input validation
        if not username_or_email or not password:
            self.display_message("Please fill in both fields.", error=True)
            return

        # Validate login credentials
        is_valid = validate_login(username_or_email, password)

        if is_valid:
            self.display_message("Login successful!", error=False)
            messagebox.showinfo("Success", "You have successfully logged in.")
            self.clear_fields()
        else:
            self.display_message("Invalid username/email or password.", error=True)

    def clear_fields(self):
        self.entry_user.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.display_message("")

    def display_message(self, message, error=True):
        self.label_message.config(text=message, fg='red' if error else 'green')


def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()