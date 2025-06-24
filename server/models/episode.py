from server.models import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date
        }