from flask_sqlalchemy import SQLAlchemy
from server.models import db  # Import db directly from server.models

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)  # Updated to Text to avoid length issues

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
