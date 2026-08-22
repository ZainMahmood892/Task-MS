# Python Tkinter Login App with MySQL

## Overview
This project is a simple login application implemented using Core Python, Tkinter for the GUI, and MySQL as the backend database. It securely handles user authentication with bcrypt password hashing and protects against SQL injection through parameterized queries.

## Features
- User login form with basic input validation.
- Secure password storage and verification using bcrypt.
- MySQL database connection using `mysql-connector-python`.
- Separation of concerns via modules: database connection, authentication logic, and GUI.

---

## Setup Instructions

### 1. MySQL Database Setup

1. Log in to your MySQL server:
```sh
mysql -u root -p
```

2. Create a database for the application (replace `your_db_name` with your desired name):
```sql
CREATE DATABASE your_db_name;
USE your_db_name;
```

3. Create a users table:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARBINARY(255) NOT NULL
);
```

4. Add a test user.

The preferred and less error-prone approach is to use the Python `auth.py` script to generate the hashed password and insert the user directly using Python. This method prevents encoding and escaping issues that can occur when inserting raw bytes via SQL.

Example Python snippet to generate hash:
```python
from auth import hash_password

hashed_pw = hash_password('yourpassword')
print(hashed_pw)
```

Then insert the user with this Python snippet:
```python
import mysql.connector
from auth import hash_password

conn = mysql.connector.connect(host='localhost', user='youruser', password='yourpass', database='your_db_name')
cursor = conn.cursor()

username = 'testuser'
password = 'yourpassword'
hashed = hash_password(password)

query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
cursor.execute(query, (username, hashed))
conn.commit()
cursor.close()
conn.close()
```

If you must insert directly via SQL, ensure the `password_hash` is inserted as raw bytes using the `_binary` keyword, but this approach is more error-prone and not recommended.

### 2. Environment Variables Setup

Set environment variables to avoid hardcoding credentials. On Linux/macOS:
```bash
export DB_HOST=localhost
export DB_USER=youruser
export DB_PASSWORD=yourpass
export DB_NAME=your_db_name
```
On Windows CMD:
```cmd
set DB_HOST=localhost
set DB_USER=youruser
set DB_PASSWORD=yourpass
set DB_NAME=your_db_name
```

### 3. Install Dependencies

Use `pip` to install required packages:
```sh
pip install -r requirements.txt
```

### 4. Run the Application

Navigate to the project directory and execute:
```sh
python ui.py
```

You should see a simple login window. Enter valid credentials from your database to log in.

---

## Notes
- This example assumes a simple username/password login system and does not handle user registration or password resets.
- Always protect your database credentials and consider using more robust configuration management for production.
- The application uses basic input validation; additional security checks may be necessary for production environments.

---

## License
This project is provided as-is for educational purposes.
