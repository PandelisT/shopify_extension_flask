from main import db
from datetime import datetime 
from sqlalchemy.orm import relationship
from models.CustomersHabits import customers_habits 
from models.CustomersTags import customers_tags 

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    is_active = db.Column(db.Boolean(), default=True)
    email = db.Column(db.String, nullable=False)
    customer_of = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    habits = relationship("Habit", secondary=customers_habits, back_populates="customers", uselist=True)
    tags = relationship("Tag", secondary=customers_tags, back_populates="customers")


    def __repr__(self):
        return f"<Customer {self.fname} {self.lname}>"