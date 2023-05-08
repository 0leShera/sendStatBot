from config_reader import config
import psycopg2


# Connect DB PostgresSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=config.db_host.get_secret_value(),
        port=config.db_port.get_secret_value(),
        database=config.db_name.get_secret_value(),
        user=config.db_user.get_secret_value(),
        password=config.db_password.get_secret_value()
    )
    return conn
