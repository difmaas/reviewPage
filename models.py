from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone
from zoneinfo import ZoneInfo

db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key = True)
    nama = db.Column(db.String(25), nullable = False)
    rating = db.Column(db.Integer)
    ulasan = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now(ZoneInfo('Asia/Jakarta')))