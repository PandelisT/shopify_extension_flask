from main import db
from datetime import datetime 
from sqlalchemy.orm import relationship
from models.OrdersProducts import orders_products


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    no_of_articles = db.Column(db.Integer)
    product_orders = db.relationship("Order", secondary=orders_products, back_populates="products", uselist=True)


    def __repr__(self):
        return f"<Order {self.id} {self.lname}>"