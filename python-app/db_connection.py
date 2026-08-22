import mysql.connector
from mysql.connector import Error
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'db_config.json')


def load_db_config():
    try:
        with open(CONFIG_PATH, 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        print(f"Database config file not found at {CONFIG_PATH}.")
        return None
    except json.JSONDecodeError:
        print(f"Database config file at {CONFIG_PATH} contains invalid JSON.")
        return None


def get_connection():
    """Establish and return a MySQL connection using parameters from the config file."""
    config = load_db_config()
    if not config:
        return None

    try:
        connection = mysql.connector.connect(
            host=config.get('host', 'localhost'),
            user=config.get('user'),
            password=config.get('password'),
            database=config.get('database'),
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None
