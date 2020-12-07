from main import db
from models.Customer import Customer
from models.Note import Note 

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    customer_id = db.relationship(Customer, backref="user", uselist=True)
    note_id = db.relationship(Note, backref="user", uselist=True)
    
    def __repr__(self):
        return f"<User {self.email}>"