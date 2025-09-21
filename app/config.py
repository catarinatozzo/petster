import os

DB_USER = "root"
DB_PASS = "rootpassword"
DB_NAME = "pets"
DB_HOST = "localhost"
DB_PORT = "3306"

database_url = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

sqlalchemy_url = os.getenv("SQLALCHEMY_URL", database_url)