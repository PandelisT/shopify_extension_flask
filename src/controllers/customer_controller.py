from flask import Blueprint, abort, jsonify, request
from schemas.CustomerSchema import customer_schema
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
