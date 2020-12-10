from main import db

# The association table for the many to many relationship between customers and habits
products_articles = db.Table("products_articles", db.Model.metadata,
db.Column("product_id", db.Integer, db.ForeignKey("products.id")),
db.Column("article_id", db.Integer, db.ForeignKey("articles.id"))
)

# from main import db
# # from models.Product import Product
# # from models.Article import Article

# class ProductsArticles(db.Model):
#     __tablename__ = "products_articles"

#     product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
#     article_id = db.Column(db.Integer, db.ForeignKey("articles.id"))
