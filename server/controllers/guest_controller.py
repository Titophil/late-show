from server.models import Guest, db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

guest_bp = Blueprint('guests', __name__, url_prefix="/guests")
guest_blueprint = guest_bp

@guest_blueprint.route('', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200
