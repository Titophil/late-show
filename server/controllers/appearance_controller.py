from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models import appearance, db

# Define the blueprint for appearance routes
appearance_bp = Blueprint('appearance', __name__, url_prefix='/appearances')
appearance_blueprint = appearance_bp


@appearance_blueprint.route('/', methods=['POST']) 
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new_appearance)
        db.session.commit()

        return jsonify(new_appearance.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400