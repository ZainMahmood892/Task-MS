import tkinter as tk
from tkinter import messagebox
from login_logic import verify_user


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("350x180")
        self.root.resizable(False, False)

        # Username/Email label and entry
        self.label_user = tk.Label(root, text="Username or Email:")
        self.label_user.pack(pady=(20, 5))
        self.entry_user = tk.Entry(root, width=40)
        self.entry_user.pack()

        # Password label and entry
        self.label_pass = tk.Label(root, text="Password:")
        self.label_pass.pack(pady=(10, 5))
        self.entry_pass = tk.Entry(root, show='*', width=40)
        self.entry_pass.pack()

        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        # Login button
        self.btn_login = tk.Button(button_frame, text="Login", width=12, command=self.login)
        self.btn_login.grid(row=0, column=0, padx=5)

        # Clear button
        self.btn_clear = tk.Button(button_frame, text="Clear", width=12, command=self.clear_fields)
        self.btn_clear.grid(row=0, column=1, padx=5)

    def login(self):
        username_or_email = self.entry_user.get()
        password = self.entry_pass.get()

        success, message = verify_user(username_or_email, password)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
        else:
            messagebox.showerror("Error", message)

    def clear_fields(self):
        self.entry_user.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
