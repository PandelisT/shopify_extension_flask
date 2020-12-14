from main import db

products_articles = db.Table("products_articles", db.Model.metadata,
                             db.Column("product_id", db.Integer,
                                       db.ForeignKey("products.id")),
                             db.Column("article_id", db.Integer,
                                       db.ForeignKey("articles.id")))
