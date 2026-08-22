import os
import mysql.connector
from mysql.connector import Error

# Database configuration loaded from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def get_db_connection():
    """
    Establishes and returns a new MySQL database connection using the DB_CONFIG.

    Returns:
        connection (mysql.connector.connection.MySQLConnection): MySQL connection object

    Raises:
        ValueError: If any required DB credentials are missing
        mysql.connector.Error: If there is an issue connecting to the database
    """
    # Validate DB credentials
    missing_vars = [key for key, value in DB_CONFIG.items() if not value]
    if missing_vars:
        raise ValueError(f"Missing required database configuration for: {', '.join(missing_vars)}")

    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
        else:
            raise Error("Database connection was not established.")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        raise
