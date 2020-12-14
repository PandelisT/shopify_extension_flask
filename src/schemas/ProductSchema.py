from main import ma
from models.Product import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

    orders = ma.Nested("OrderSchema", many=True)
    articles = ma.Nested("ArticleSchema", many=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
