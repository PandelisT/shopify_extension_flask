from main import ma
from models.Order import Order

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
    
    # customer = ma.Nested("CustomerSchema", many=True)


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)