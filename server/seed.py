from server.app import app, db
from server.models import User, Guest, Episode, Appearance
from werkzeug.security import generate_password_hash

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Create users
    user1 = User(username="admin", password_hash=generate_password_hash("admin123"))
    db.session.add(user1)

    # Create guests
    guest1 = Guest(name="Keanu Reeves", occupation="Actor", image_url="https://example.com/keanu.jpg")
    guest2 = Guest(name="Bill Gates", occupation="Entrepreneur", image_url="https://example.com/gates.jpg")

    # Create episodes
    episode1 = Episode(date="2023-06-01")
    episode2 = Episode(date="2023-06-02")

    # Add episodes and guests
    db.session.add_all([guest1, guest2, episode1, episode2])
    db.session.commit()

    # Create appearances
    appearance1 = Appearance(episode_id=episode1.id, guest_id=guest1.id, rating=8.7)
    appearance2 = Appearance(episode_id=episode2.id, guest_id=guest2.id, rating=9.2)

    db.session.add_all([appearance1, appearance2])
    db.session.commit()

    print("✅ Done seeding!")