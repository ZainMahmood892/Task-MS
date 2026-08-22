# Python Tkinter Login Application

This is a simple Python Tkinter login application that authenticates users against a MySQL database using secure password hashing (bcrypt) and parameterized queries.

---

## Features
- Secure password storage using bcrypt hashing
- Parameterized queries to prevent SQL injection
- Input validation on username and password
- Clean separation of concerns: DB connection, login logic, and UI

---

## Prerequisites
- Python 3.7 or higher
- MySQL server running with a database and users table

---

## Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd python-app
```

### 2. Create and Configure MySQL Database

Login to your MySQL server and create a database and users table:

```sql
CREATE DATABASE your_database;
USE your_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash BLOB NOT NULL
);
```

### 3. Create a User for Testing

You need to insert a user into the `users` table with a bcrypt hashed password.

You can generate a bcrypt hash in Python:

```python
import bcrypt

password = 'yourpassword'
hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(hash)
```

Copy the printed hash and use it in SQL:

```sql
INSERT INTO users (username, password_hash) VALUES ('testuser', _binary '<paste_hash_here>');
```

Example with python shell:

```python
import mysql.connector
import bcrypt

conn = mysql.connector.connect(host='localhost', user='your_username', password='your_password', database='your_database')
cursor = conn.cursor()

password = 'yourpassword'
hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", ('testuser', hash))
conn.commit()
cursor.close()
conn.close()
```

### 4. Set Database Configuration Using Environment Variables

Set the following environment variables in your system with your MySQL credentials:

- `DB_HOST` (optional, defaults to `localhost` if not set)
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

#### On Linux/macOS:

```bash
export DB_HOST=localhost
export DB_USER=your_username
export DB_PASSWORD=your_password
export DB_NAME=your_database
```

#### On Windows CMD:

```cmd
set DB_HOST=localhost
set DB_USER=your_username
set DB_PASSWORD=your_password
set DB_NAME=your_database
```

#### On Windows PowerShell:

```powershell
$env:DB_HOST="localhost"
$env:DB_USER="your_username"
$env:DB_PASSWORD="your_password"
$env:DB_NAME="your_database"
```

### 5. Install Python Dependencies

It's recommended to use a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python ui.py
```

A small login window will appear. Enter your username and password to authenticate.

---

## Notes
- This example is usable as a learning tool or starting point; consider additional security measures for production.
- Passwords are securely hashed, and database queries are parameterized.
- The UI uses Tkinter for simplicity.

---

## License
MIT License

---

If you encounter any issues or have suggestions, feel free to open an issue or contribute!
