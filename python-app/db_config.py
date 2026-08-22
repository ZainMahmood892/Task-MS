import mysql.connector
from mysql.connector import Error

# Database configuration
HOST = 'localhost'
USER = 'root'
PASSWORD = ''  # Set your MySQL password
DATABASE = 'login_app'


def get_db_connection():
    """
    Creates and returns a new MySQL database connection.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object

    Raises:
        mysql.connector.Error: When failed to connect
    """
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        raise

    return None


if __name__ == '__main__':
    # Simple self-test
    conn = None
    try:
        conn = get_db_connection()
        if conn:
            print("Successfully connected to the database.")
    finally:
        if conn and conn.is_connected():
            conn.close()