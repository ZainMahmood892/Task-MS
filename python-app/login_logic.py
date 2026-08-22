import bcrypt
from db_connection import get_connection


def sanitize_input(user_input):
    """Basic sanitization: strip whitespace."""
    if not isinstance(user_input, str):
        return ''
    return user_input.strip()


def verify_user(username_or_email, password):
    """
    Verify if the user with the given username or email exists and the password matches.
    Returns tuple (success: bool, message: str).
    """
    username_or_email = sanitize_input(username_or_email)
    if not username_or_email:
        return False, "Username/Email cannot be empty."

    if not password:
        return False, "Password cannot be empty."

    conn = get_connection()
    if not conn:
        return False, "Database connection failed."

    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT password FROM users 
            WHERE username = %s OR email = %s
            LIMIT 1
        """
        cursor.execute(query, (username_or_email, username_or_email))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if not user:
            return False, "User not found."

        hashed_password = user['password'].encode('utf-8')
        # bcrypt expects bytes passwords
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True, "Login successful!"
        else:
            return False, "Incorrect password."

    except Exception as e:
        return False, f"An error occurred: {str(e)}"
