import bcrypt
from db_config import get_db_connection
from mysql.connector import Error


def validate_login(username_or_email: str, password: str) -> bool:
    """
    Validates the login credentials against the users table in the database.

    Args:
        username_or_email (str): Username or Email entered by the user.
        password (str): Plain text password entered by the user.

    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    if not username_or_email or not password:
        return False

    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Parameterized query to prevent SQL injection
        query = """
            SELECT password_hash FROM users
            WHERE username = %s OR email = %s
            LIMIT 1
        """
        cursor.execute(query, (username_or_email, username_or_email))

        user = cursor.fetchone()

        if user is None:
            return False

        stored_hash = user['password_hash']

        # bcrypt requires bytes
        password_bytes = password.encode('utf-8')
        stored_hash_bytes = stored_hash.encode('utf-8')

        if bcrypt.checkpw(password_bytes, stored_hash_bytes):
            return True

        return False

    except Error as e:
        print(f"Database error during login validation: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()