from main import db
from datetime import datetime
from models.OrdersProducts import orders_products


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime(), nullable=False,
                           default=datetime.now)
    customer_of = db.Column(db.Integer, db.ForeignKey("users.id"),
                            nullable=False)
    products = db.relationship("Product", secondary=orders_products,
                               back_populates="product_orders", uselist=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"),
                            nullable=False)

    def __repr__(self):
        return f"<Order {self.id}>"
