from main import db

# The association table for the many to many relationship between customers and Tags
customers_tags = db.Table("customers_tags", db.Model.metadata,
db.Column("customer_id", db.Integer, db.ForeignKey("customers.id")),
db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"))
)
