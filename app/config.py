import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    # MySQL connection URI format:
    # mysql+pymysql://<username>:<password>@<host>/<database>
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost/charity"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
