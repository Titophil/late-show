from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

__all__ = ["User", "Guest", "Episode", "Appearance", "db"]