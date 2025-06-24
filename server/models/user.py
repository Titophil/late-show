# server/models/user.py
# Import the shared 'db' instance from server.models.__init__.py
from .__init__ import db # Or simply: from server.models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'
