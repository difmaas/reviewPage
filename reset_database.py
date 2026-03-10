
from app import db, app  # pastikan import db dan Flask app yang sama

with app.app_context():
    db.create_all()  # bikin semua tabel dari model SQLAlchemy
print("Tabel baru sudah dibuat")