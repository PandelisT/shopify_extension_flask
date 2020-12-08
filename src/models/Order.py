from main import db
from datetime import datetime 
from sqlalchemy.orm import relationship


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    customer_of = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    products = relationship("Product", secondary=orders_products, back_populates="customers")


    def __repr__(self):
        return f"<Order {self.id} {self.lname}>"