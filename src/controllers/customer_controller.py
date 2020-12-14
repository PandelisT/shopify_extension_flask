from flask import Blueprint, abort, jsonify, request
from schemas.CustomerSchema import customer_schema, customers_schema
from models.Customer import Customer
from models.User import User
from main import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


customer = Blueprint("customer", __name__, url_prefix="/customer")


@customer.route("/", methods=["POST"])
@jwt_required
def new_customer():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    customer_fields = customer_schema.load(request.json)

    try:
        new_customer = Customer()
        new_customer.fname = customer_fields["fname"]
        new_customer.lname = customer_fields["lname"]
        new_customer.email = customer_fields["email"]
        new_customer.is_active = customer_fields["is_active"]
        user.customer_id.append(new_customer)

        db.session.add(new_customer)
        db.session.commit()

        return jsonify(customer_schema.dump(new_customer))

    except Exception:
        return abort(400, "You missed one or more fields")


@customer.route("/", methods=["GET"])
@jwt_required
def get_customers_for_user():
    # Get all customers for logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    all_customers = Customer.query.filter_by(
        customer_of=user.id).all()

    if all_customers == []:
        return abort(401, description="No customers for user")

    return jsonify(customers_schema.dump(all_customers))


@customer.route("/<int:customer_id>", methods=["GET"])
@jwt_required
def get_customer(customer_id):
    # gets a customer for a user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    customer = Customer.query.filter_by(customer_of=user.id,
                                        id=customer_id).all()

    if customer == []:
        return abort(401, description="Invalid customer")

    return jsonify(customers_schema.dump(customer))


@customer.route("/<int:customer_id>", methods=["DELETE"])
@jwt_required
def delete_customer(customer_id):
    # Deletes a customer
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    customer = Customer.query.filter_by(customer_of=user.id,
                                        id=customer_id).first()

    if not customer:
        return abort(401, description="Invalid customer")

    db.session.delete(customer)
    db.session.commit()

    return jsonify("The following customer was deleted from the database.",
                   customer_schema.dump(customer))


@customer.route("/<int:customer_id>", methods=["PUT"])
@jwt_required
def update_customer(customer_id):
    # Updates customer details
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    customer_fields = customer_schema.load(request.json)
    customer = Customer.query.filter_by(customer_of=user.id, id=customer_id)

    if customer.count() != 1:
        return abort(404, description="Not a valid customer")

    customer.fname = customer_fields["fname"]
    customer.lname = customer_fields["lname"]
    customer.email = customer_fields["email"]
    customer.is_active = customer_fields["is_active"]

    customer.update(customer_fields)
    db.session.commit()

    return jsonify(customer_schema.dump(customer))
