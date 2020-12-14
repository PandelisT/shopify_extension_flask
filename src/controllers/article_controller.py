from flask import Blueprint, abort, jsonify, request
from schemas.ProductSchema import product_schema
from schemas.ArticleSchema import article_schema
from models.User import User
from models.Product import Product
from models.Article import Article
from main import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


article = Blueprint("article", __name__, url_prefix="/article")


@article.route("/", methods=["POST"])
@jwt_required
def new_article():
    # Creates a new article for logged in user
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


@article.route("/<int:article_id>", methods=["GET"])
@jwt_required
def get_article(article_id):
    # Gets an article for logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    article = Article.query.filter_by(id=article_id).first()

    if not article:
        return abort(401, description="Invalid article")

    return jsonify(article_schema.dump(article))


@article.route("/<int:article_id>", methods=["PUT"])
@jwt_required
def update_article(article_id):
    # Updates an article for logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    article_fields = article_schema.load(request.json)
    article = Article.query.filter_by(id=article_id)

    if article.count() != 1:
        return abort(404, description="Article not found.")

    article.title = article_fields["title"]
    article.body_html = article_fields["body_html"]
    article.summary = article_fields["summary"]
    article.allow_comments = article_fields["allow_comments"]
    article.custom_post_type = article_fields["custom_post_type"]
    article.show_date_and_author = article_fields["show_date_and_author"]
    article.show_summary = article_fields["show_summary"]

    article.update(article_fields)
    db.session.commit()

    return jsonify(article_schema.dump(article))


@article.route("/product/<int:product_id>/article_id/<int:article_id>",
               methods=["POST"])
@jwt_required
def new_article_product(product_id, article_id):
    # Adds a product to a article of the user logged in
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    product = Product.query.filter_by(id=product_id).first()
    article = Article.query.filter_by(id=article_id).first()
    article.articles.append(product)
    db.session.add(product)
    db.session.commit()

    return jsonify(product_schema.dump(product))


@article.route("/<int:article_id>", methods=["DELETE"])
@jwt_required
def delete_article(article_id):
    # Deletes an article for logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    article = Article.query.filter_by(id=article_id).first()

    if not article:
        return abort(401, description="Invalid article")

    db.session.delete(article)
    db.session.commit()

    return jsonify("The following article was deleted from the database.",
                   article_schema.dump(article))
