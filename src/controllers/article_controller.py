from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.OrderSchema import order_schema, orders_schema
from schemas.ProductSchema import product_schema, products_schema
from schemas.ArticleSchema import article_schema, articles_schema
from models.User import User
from models.Customer import Customer
from models.Order import Order
from models.Product import Product
from models.Article import Article
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta
from sqlalchemy import text


article = Blueprint("article", __name__, url_prefix="/article")


@article.route("/", methods=["POST"])
@jwt_required
def new_article():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    article_fields = article_schema.load(request.json)
    
    new_article = Article()
    new_article.title = article_fields["title"]
    new_article.body_html = article_fields["body_html"]
    new_article.summary = article_fields["summary"]
    new_article.allow_comments = article_fields["allow_comments"]
    new_article.custom_post_type = article_fields["custom_post_type"]
    new_article.show_date_and_author = article_fields["show_date_and_author"]
    new_article.show_summary = article_fields["show_summary"]

    user.article_id.append(new_article)


    db.session.add(new_article)
    db.session.commit()
        
    return jsonify(article_schema.dump(new_article))


@article.route("/product/<int:product_id>/article_id/<int:article_id>", methods=["POST"])
@jwt_required
def new_article_product(product_id, article_id):
    # Adds a product to a article
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    product = Product.query.filter_by(id = product_id).first()
    article = Article.query.filter_by(id = article_id).first()
    article.articles.append(product)
        
    db.session.add(product)
    db.session.commit()
        
    return jsonify(product_schema.dump(product))