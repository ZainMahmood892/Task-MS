import bcrypt
from db import get_db_connection


def hash_password(plain_password: str) -> bytes:
    """Hash a plaintext password using bcrypt."""
    # bcrypt requires bytes
    password_bytes = plain_password.encode('utf-8')
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """Verify a plaintext password against a hashed password."""
    password_bytes = plain_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)


def get_user_hashed_password(username: str):
    """Retrieve hashed password for a given username from the DB.
    Returns bytes (hashed password) or None if user not found.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor(buffered=True)
        query = "SELECT password_hash FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            # Stored as bytes, so return as bytes
            return row[0]
        return None
    finally:
        cursor.close()
        conn.close()


def verify_login(username: str, password: str) -> bool:
    """Check if provided username and password are correct."""
    if not username or not password:
        return False
    try:
        hashed = get_user_hashed_password(username)
        if hashed is None:
            return False
        # MySQL stores VARBINARY or BLOB as bytes, but if stored as string, decode needed
        # Assuming password_hash column type VARBINARY/BLOB
        return verify_password(password, hashed)
    except Exception as e:
        print(f"Exception during login verification: {e}")
        return False
