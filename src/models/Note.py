from main import db
from datetime import datetime
from models.Customer import Customer
from sqlalchemy.orm import relationship


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    comms_type = db.Column(db.String(), nullable=False)
    note = db.Column(db.String(), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Note {self.id}>"