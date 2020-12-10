from main import db
from datetime import datetime 
from sqlalchemy.orm import relationship
from models.OrdersProducts import orders_products
from models.ProductsArticles import products_articles
from models.Article import Article


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    no_of_articles = db.Column(db.Integer(), default=0)
    articles = db.relationship("Article", secondary=products_articles, back_populates="articles", uselist=True)
    product_orders = db.relationship("Order", secondary=orders_products, back_populates="products", uselist=True)

    @classmethod
    def article_count(cls):
        return db.engine.execute('select count(id) from products_articles where product_id = id').scalar()

    @classmethod
    def article_filter_count(cls, product_id):
        sql_query = text("SELECT count(id) FROM WHERE product_id=':product_id';")
        return db.engine.execute(sql_query, {"customer_id": customer_id, "user_id": user_id})


    def __repr__(self):
        return f"<Product {self.id}>"