from main import db

# The association table for the many to many relationship between customers and habits
orders_products = db.Table("orders_products", db.Model.metadata,
db.Column("order_id", db.Integer, db.ForeignKey("orders.id")),
db.Column("product_id", db.Integer, db.ForeignKey("products.id"))
)