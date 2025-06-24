from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash

from server.config import Config
from server.models import db  # Shared db instance
from server.models.user import User  # Import User model

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

# Test route: Create user (for Postman testing)
@app.route('/')
def index():
    return {'message': 'Late Show API is running.'}, 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201
