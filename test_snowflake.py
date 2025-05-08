import snowflake.connector
from decouple import config

SNOWFLAKE_CONFIG = {
    'user': config('SNOWFLAKE_USER'),
    'password': config('SNOWFLAKE_PASSWORD'),
    'account': config('SNOWFLAKE_ACCOUNT'),
    'database': config('SNOWFLAKE_DATABASE'),
    'schema': config('SNOWFLAKE_SCHEMA'),
    'role': config('SNOWFLAKE_ROLE'),
}

try:
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION()")
    version = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM products LIMIT 1")
    sample_row = cursor.fetchone()
    print(f"Connected to Snowflake! Version: {version}")
    print(f"Sample product row: {sample_row}")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Connection failed: {str(e)}")