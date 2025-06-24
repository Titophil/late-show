from server.models import db


class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Use string references for relationships to avoid circular dependencies
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    def to_dict(self):
        return {
            "id": self.id,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id,
            "rating": self.rating
        }