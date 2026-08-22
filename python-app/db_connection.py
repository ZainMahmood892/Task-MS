import os
import logging
import mysql.connector
from mysql.connector import Error

logging.basicConfig(level=logging.ERROR)


def get_connection():
    host = os.getenv('DB_HOST', 'localhost')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    if not user or not password or not database:
        logging.error("Database credentials are not fully set in environment variables.")
        raise EnvironmentError("Database credentials are not fully set in environment variables.")

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            return connection
    except Error as e:
        logging.error(f"Error while connecting to MySQL: {e}")
        raise

    raise ConnectionError("Failed to connect to the database.")
