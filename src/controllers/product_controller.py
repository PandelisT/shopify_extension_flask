from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.OrderSchema import order_schema, orders_schema
from schemas.ProductSchema import product_schema, products_schema
from models.User import User
from models.Customer import Customer
from models.Order import Order
from models.Product import Product
from models.ProductsArticles import products_articles
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta
from sqlalchemy import text, func
from sqlalchemy.orm import sessionmaker


product = Blueprint("product", __name__, url_prefix="/product")


@product.route("/", methods=["POST"])
@jwt_required
def new_product():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    product_fields = product_schema.load(request.json)
    
    new_product = Product()
    new_product.title = product_fields["title"]
    new_product.description = product_fields["description"]
    new_product.quantity = product_fields["quantity"]
    new_product.price = product_fields["price"]

    user.product_id.append(new_product)
    
    db.session.add(new_product)
    db.session.commit()
        
    return jsonify(product_schema.dump(new_product))

@product.route("/<int:product_id>/order/<int:order_id>", methods=["POST"])
@jwt_required
def add_product_to_order(product_id, order_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    product = Product.query.filter_by(id = product_id).first()
    order = Order.query.filter_by(id = order_id).first()

    print(product)
    print(order)

    if not product  or not order:
        return abort(403, description="Incorrect product or order")

    order.products.append(product)
        
    db.session.add(product)
    db.session.commit()
        
    return jsonify(product_schema.dump(product))

@product.route("/<int:product_id>", methods=["PUT"])
@jwt_required
def update_product(product_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    product_fields = product_schema.load(request.json)
    
    new_product = Product()
    new_product.title = product_fields["title"]
    new_product.description = product_fields["description"]
    new_product.quantity = product_fields["quantity"]
    new_product.price = product_fields["price"]
    new_product.no_of_articles = db.session.query(db.Model.metadata.tables['products_articles']).filter(product_id == product_id).count()
    
    user.product_id.append(new_product)
    
    db.session.add(new_product)
    db.session.commit()
        
    return jsonify(product_schema.dump(new_product))