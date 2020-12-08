from main import ma
from models.Product import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
    
    # customer = ma.Nested("CustomerSchema", many=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)