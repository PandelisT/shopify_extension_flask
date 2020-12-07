from flask import Blueprint, abort, jsonify, request
from schemas.CustomerSchema import customer_schema, customers_schema
from models.Customer import Customer
from models.User import User
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta


customer = Blueprint("customer", __name__, url_prefix="/customer")


@customer.route("/", methods=["POST"])
@jwt_required
def new_account():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    customer_fields = customer_schema.load(request.json)
    
    new_customer = Customer()
    new_customer.fname = customer_fields["fname"]
    new_customer.lname = customer_fields["lname"]
    new_customer.address = customer_fields["address"]
    new_customer.email = customer_fields["email"]
    new_customer.is_active= customer_fields["is_active"]

    user.customer_id.append(new_customer)
        
    db.session.add(new_customer)
    db.session.commit()
        
    return jsonify(customer_schema.dump(new_customer))

@customer.route("/", methods=["GET"])
@jwt_required
def get_customers_for_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    all_customers = Customer.query.filter_by(customer_of=user.id)
    return jsonify(customers_schema.dump(all_customers))

@customer.route("/<int:customer_id>", methods=["GET"])
@jwt_required
def get_customer(customer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    all_customers = Customer.query.filter_by(customer_of=user.id, id = customer_id)
    return jsonify(customers_schema.dump(all_customers))