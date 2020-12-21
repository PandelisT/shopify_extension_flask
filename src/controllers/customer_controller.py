from flask import Blueprint, abort, jsonify, request, render_template, redirect
from schemas.CustomerSchema import CustomerSchema, customer_schema, customers_schema
from schemas.UserSchema import UserSchema, users_schema, user_schema
from schemas.AddressSchema import address_schema
from schemas.ArticleSchema import articles_schema
from schemas.HabitSchema import habits_schema
from schemas.NoteSchema import notes_schema
from schemas.OrderSchema import orders_schema
from schemas.ProductSchema import products_schema
from schemas.TagSchema import tags_schema
from models.Customer import Customer
from models.User import User
from main import db
from flask_jwt_extended import jwt_required
import flask_jwt_extended
from flask_jwt_extended import get_jwt_identity, create_access_token
from datetime import datetime
import json


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
def get_all_customers_for_user_api():
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


@customer.route("/dump", methods=["GET"])
@jwt_required
def dump_all_customers_info_for_user():
    # Get all customers for logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    all_tables = ["addresses", "articles", "customers", "habits", "notes", "orders", "products", "tags", "users"]
    schemas = [address_schema, articles_schema, customers_schema, habits_schema, notes_schema, orders_schema, products_schema, tags_schema, users_schema ]
    i = 0
    for table in all_tables:
        query = db.engine.execute(f'SELECT * FROM {table}')
        data = ((schemas[i]).dump(query))
        data = json.dumps(data)
        i+=1
    
        file = open("src/dump/dump.json", "a")
        file.write(data)
        file.close()

    return "All table data dumped to src/dump/dump.json"

@customer.route("/user/<int:user_id>", methods=["GET"])
@jwt_required
def get_customers_for_user(user_id):
    # Get all customers for logged in user and renders on index.html page
    jwt_user = get_jwt_identity()
    user = User.query.get(jwt_user)
    if not user:
        return abort(401, description="Invalid user")

    user_dump = UserSchema().dump(user)

    all_customers = Customer.query.all()
    customer_dump = CustomerSchema(many=True).dump(all_customers)

    logged_in_user = flask_jwt_extended.get_jwt_identity()

    if logged_in_user == user.id:
        return render_template("index.html", customers=customer_dump, user=user_dump, auth=True)

    return render_template('index.html', customers=customer_dump)

@customer.route("/user/<int:user_id>", methods=["POST"])
@jwt_required
def new_customers_for_user(user_id):
    # Add customer on index.html
    jwt_id = get_jwt_identity()
    user = User.query.get(jwt_id)
    if not user:
        return abort(401, description="Invalid user")
    
    logged_in_user = flask_jwt_extended.get_jwt_identity()

    access_token = create_access_token(identity=str(user.id))

    if logged_in_user == user.id:
        data = request.form.to_dict()
        customer_fields = CustomerSchema().load(data)
        new_customer = Customer(fname=customer_fields["fname"], lname=customer_fields["lname"], is_active=customer_fields["is_active"], email=customer_fields["email"], customer_of=user.id,
        headers={"Authorization": f"Bearer {access_token}"})
        
        db.session.add(new_customer)
        db.session.commit()

    return redirect(f"customer/user/{user_id}", code=302)

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



