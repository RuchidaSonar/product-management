from decouple import config

SNOWFLAKE_CONFIG = {
    'user': config('SNOWFLAKE_USER'),
    'password': config('SNOWFLAKE_PASSWORD'),
    'account': config('SNOWFLAKE_ACCOUNT'),
    'database': config('SNOWFLAKE_DATABASE'),
    'schema': config('SNOWFLAKE_SCHEMA'),
    'role': config('SNOWFLAKE_ROLE'),
}