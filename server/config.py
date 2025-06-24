import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "postgresql://titus_user:my_secure_password@localhost:5432/late_show_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "4f9a69789c1a4c5f8e6cba723c770f3bd26e2ae59d78c2180d4bff814b07c6a6"  # secure 64-char hex
    )
