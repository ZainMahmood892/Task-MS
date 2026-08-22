import re
from db_connection import get_db_connection
import bcrypt


def validate_username(username):
    """
    Validates the username input.

    Args:
        username (str): The username string to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(username, str):
        return False
    username = username.strip()
    # Username must be 3-30 characters, alphanumeric and underscores only
    pattern = r'^[a-zA-Z0-9_]{3,30}$'
    return re.match(pattern, username) is not None


def validate_password(password):
    """
    Validates the password input.

    Args:
        password (str): The password string to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(password, str):
        return False
    # Password must be at least 8 characters long
    return len(password) >= 8


def hash_password(raw_password):
    """
    Hashes the password using bcrypt.

    Args:
        raw_password (str): The plain text password

    Returns:
        str: The hashed password (utf-8 encoded string)
    """
    # bcrypt requires bytes
    hashed = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(raw_password, hashed_password):
    """
    Verifies a raw password against the hashed password using bcrypt.

    Args:
        raw_password (str): The plain text password
        hashed_password (str): The hashed password stored

    Returns:
        bool: True if match, False otherwise
    """
    try:
        return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return False


def authenticate_user(username, password):
    """
    Authenticates a user by validating inputs and checking credentials from the database.

    Args:
        username (str): Username input
        password (str): Password input

    Returns:
        tuple: (bool success, str message)
            success - True if authentication passed
            message - Informative message for UI
    """
    # Validate inputs
    if not validate_username(username):
        return False, "Invalid username. Must be 3-30 alphanumeric characters or underscores."
    if not validate_password(password):
        return False, "Invalid password. Must be at least 8 characters long."

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # Use parameterized query for security
        query = "SELECT username, password_hash FROM users WHERE username = %s LIMIT 1"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user is None:
            return False, "User not found."

        stored_hash = user['password_hash']
        if verify_password(password, stored_hash):
            return True, "Login successful."
        else:
            return False, "Incorrect password."

    except Exception as e:
        # Log error in production environment instead of printing
        return False, "An error occurred during authentication."