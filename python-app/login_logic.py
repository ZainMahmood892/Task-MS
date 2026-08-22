import re
import bcrypt
from db_connection import get_connection


def validate_inputs(username: str, password: str):
    errors = []
    if not username or not username.strip():
        errors.append("Username cannot be empty.")
    if not password:
        errors.append("Password cannot be empty.")
    if len(username) < 3 or len(username) > 50:
        errors.append("Username must be between 3 and 50 characters.")
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")
    # Optionally, more regex checks can be implemented here.
    return errors


def login(username: str, password: str):
    # Input validation
    errors = validate_inputs(username, password)
    if errors:
        return False, " ".join(errors)

    # Open database connection
    conn = get_connection()
    if not conn:
        return False, "Database connection error."

    try:
        cursor = conn.cursor(prepared=True)
        query = "SELECT password_hash FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row is None:
            return False, "Invalid username or password."

        stored_hash = row[0]
        if isinstance(stored_hash, memoryview):
            stored_hash = stored_hash.tobytes()
        # Ensure stored_hash is bytes
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode('utf-8')

        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            return True, "Login successful."
        else:
            return False, "Invalid username or password."
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"
    finally:
        cursor.close()
        conn.close()
