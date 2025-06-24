from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from server.config import Config
from server.models import db  # Import the shared db instance

# Controllers
from server.controllers.auth_controller import auth_blueprint
from server.controllers.episode_controller import episode_blueprint
from server.controllers.guest_controller import guest_blueprint
from server.controllers.appearance_controller import appearance_blueprint

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(episode_blueprint)
app.register_blueprint(guest_blueprint)
app.register_blueprint(appearance_blueprint)