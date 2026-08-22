# Python Tkinter Login Application with MySQL

This project is a simple Python Tkinter application to perform user login by verifying credentials from a MySQL database using secure password hashing and parameterized queries.

---

## Features
- User login with Username or Email and Password
- Secure password hashing with bcrypt
- Parameterized SQL queries to prevent SQL injection
- Clear and login buttons with informative message display

---

## Prerequisites
- Python 3.6 or newer installed
- MySQL Server installed and running

---

## Step 1: Create the MySQL Database and Users Table

1. Log in to your MySQL server:
   ```
   mysql -u root -p
   ```

2. Create a new database (for example `login_app`):
   ```sql
   CREATE DATABASE login_app;
   USE login_app;
   ```

3. Create the `users` table with the following structure:
   ```sql
   CREATE TABLE users (
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE NOT NULL,
       email VARCHAR(100) UNIQUE NOT NULL,
       password_hash VARCHAR(255) NOT NULL
   );
   ```

4. Insert sample user data with hashed passwords. To generate hashed passwords, you can use the Python bcrypt library or manually insert one. For example:

   - Run Python interactive shell (or a script) to generate a hashed password:
     ```python
     import bcrypt

     password = b"Password123!"
     hashed = bcrypt.hashpw(password, bcrypt.gensalt())
     print(hashed.decode())
     ```

   - Then insert a user:
     ```sql
     INSERT INTO users (username, email, password_hash) VALUES
     ('testuser', 'testuser@example.com', '$2b$12$yourhashedpasswordstringhere');
     ```

Replace `'$2b$12$yourhashedpasswordstringhere'` with the output from the Python bcrypt hash.

---

## Step 2: Install Required Python Packages

It's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

Install required packages:

```bash
pip install mysql-connector-python bcrypt
```

---

## Step 3: Configure Database Connection

Edit the file `python-app/db_config.py` to set your MySQL hostname, username, password, and database name.

Example:

```python
HOST = 'localhost'
USER = 'root'
PASSWORD = 'your_mysql_password'
DATABASE = 'login_app'
```

---

## Step 4: Run the Application

From the `python-app` directory, run:

```bash
python login_ui.py
```

This will launch the Tkinter login window.

---

## Usage Notes
- Enter your username or email.
- Enter the password.
- Click **Login** to authenticate.
- Click **Clear** to reset fields.
- Message area below buttons shows success or error messages.

---

## Security Notes
- Passwords are hashed with bcrypt before storing in the database.
- Login uses secure parameterized queries to prevent SQL injection.
- Passwords are never stored or transmitted in plain text.


---

If you encounter any issues or have questions, please ensure your Python environment is set up correctly, and that the MySQL service is running with correct access credentials.

Enjoy your secure login app!