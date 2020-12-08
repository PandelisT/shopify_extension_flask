from datetime import datetime 
from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    no_of_articles = db.Column(db.Integer)
    orders = relationship("Order", secondary=orders_products, back_populates="orders")


    def __repr__(self):
        return f"<Order {self.id} {self.lname}>"