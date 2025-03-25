from database import db
from datetime import datetime, timezone

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    created_in = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    diet = db.Column(db.String(80), nullable=False, default=True)

    """def __init__(self, id, name, description, created_in, diet=True) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.diet = diet
        self.created_in = created_in


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "diet": self.diet,
            "created in": self.created_in
        }"""
        