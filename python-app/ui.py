import tkinter as tk
from tkinter import messagebox
from login_logic import login


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("300x180")
        self.root.resizable(False, False)

        self.frame = tk.Frame(root, padx=15, pady=15)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.label_user = tk.Label(self.frame, text="Username:")
        self.label_user.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))

        self.entry_user = tk.Entry(self.frame)
        self.entry_user.grid(row=0, column=1, pady=(0, 10))
        self.entry_user.focus()

        self.label_pass = tk.Label(self.frame, text="Password:")
        self.label_pass.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))

        self.entry_pass = tk.Entry(self.frame, show='*')
        self.entry_pass.grid(row=1, column=1, pady=(0, 10))

        self.btn_login = tk.Button(self.frame, text="Login", command=self.attempt_login)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.attempt_login())

    def attempt_login(self):
        username = self.entry_user.get().strip()
        password = self.entry_pass.get()

        success, message = login(username, password)

        if success:
            messagebox.showinfo("Success", message)
            # Could clear inputs or close app here
            self.entry_user.delete(0, tk.END)
            self.entry_pass.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)


def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
