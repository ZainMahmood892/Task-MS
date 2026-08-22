import mysql.connector
import os


def get_db_connection():
    """Establish and return a new MySQL database connection."""
    # Retrieve database credentials from environment variables
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')

    # Validate required environment variables, fail loudly if not set
    missing_vars = []
    if not db_user:
        missing_vars.append('DB_USER')
    if not db_password:
        missing_vars.append('DB_PASSWORD')
    if not db_name:
        missing_vars.append('DB_NAME')

    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

    db_config = {
        'host': db_host,
        'user': db_user,
        'password': db_password,
        'database': db_name,
        'auth_plugin': 'mysql_native_password'
    }

    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        raise
