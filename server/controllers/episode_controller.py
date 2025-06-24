from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models import Episode, db, Appearance

episode_blueprint = Blueprint('episodes', __name__, url_prefix="/episodes")

@episode_blueprint.route('', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in episodes]), 200

@episode_blueprint.route('/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({"message": "Episode not found"}), 404

    appearances = Appearance.query.filter_by(episode_id=episode_id).all()
    appearances_data = [appearance.to_dict() for appearance in appearances]

    response = episode.to_dict()
    response['appearances'] = appearances_data

    return jsonify(response), 200

@episode_blueprint.route('/<int:episode_id>', methods=['DELETE'])
@jwt_required()
def delete_episode(episode_id):
    ep = Episode.query.get(episode_id)
    if not ep:
        return jsonify({"message": "Episode not found"}), 404

    if ep.appearances:
        return jsonify({"message": "Cannot delete episode with appearances"}), 400

    db.session.delete(ep)
    db.session.commit()
    return jsonify({"message": "Episode deleted successfully"}), 200
