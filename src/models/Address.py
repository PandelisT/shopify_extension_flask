from main import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime(), nullable=False,
                           default=datetime.now)
    number = db.Column(db.Integer, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(), nullable=False)
    suburb = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    customer_address = relationship("Customer", back_populates="address")

    def __repr__(self):
        return f"<Address {self.id}>"
