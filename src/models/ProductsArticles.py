from main import db

# The association table for the many to many relationship between customers and habits
products_articles = db.Table("products_articles", db.Model.metadata,
db.Column("product_id", db.Integer, db.ForeignKey("productss.id")),
db.Column("article_id", db.Integer, db.ForeignKey("articles.id"))
)