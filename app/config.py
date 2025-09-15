import os

db_user = os.getenv("DB_USER", os.getenv("MYSQL_USER", "root"))
db_pass = os.getenv("DB_PASS", os.getenv("MYSQL_PASSWORD", "senha"))
db_name = os.getenv("DB_NAME", os.getenv("MYSQL_DATABASE", "petster"))
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "3306")
database_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
