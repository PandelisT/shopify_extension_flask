from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.OrderSchema import order_schema, orders_schema
from schemas.ProductSchema import product_schema, products_schema
from schemas.ArticleSchema import article_schema, articles_schema
from schemas.AddressSchema import address_schema
from models.User import User
from models.Customer import Customer
from models.Order import Order
from models.Product import Product
from models.Article import Article
from models.Address import Address
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta
from sqlalchemy import text


address = Blueprint("address", __name__, url_prefix="/address")


@address.route("/customer/<int:customer_id>", methods=["POST"])
@jwt_required
def new_address_for_customer(customer_id):
    # Add new address for customer
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    address_fields = address_schema.load(request.json)
    
    try: 
        new_address = Address()
        new_address.number = address_fields["number"]
        new_address.postcode = address_fields["postcode"]
        new_address.street = address_fields["street"]
        new_address.suburb = address_fields["suburb"]
        new_address.state = address_fields["state"]
        new_address.customer_id = customer_id
        new_address.user_id = user.id

        customer = Customer.query.filter_by(customer_of = user.id, id = customer_id).first()
        customer.address=new_address

        db.session.add(new_address)
        db.session.commit()
            
        return jsonify(address_schema.dump(new_address))
    
    except:
        return abort (400, "You missed one or more fields")

@address.route("/<int:address_id>", methods=["GET"])
@jwt_required
def get_address(address_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    address = Address.query.filter_by(id = address_id).first()

    if not address:
        return abort(401, description="Invalid address")

    return jsonify(address_schema.dump(address))

@address.route("/<int:address_id>", methods=["DELETE"])
@jwt_required
def delete_address(address_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    address = Address.query.filter_by(id = address_id).first()

    if not address:
        return abort(401, description="Invalid address")

    db.session.delete(address)
    db.session.commit()

    return jsonify("The following address was deleted from the database.", address_schema.dump(address))
