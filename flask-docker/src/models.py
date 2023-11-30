# models.py
from src.extensions import db

class TaskResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(255))
