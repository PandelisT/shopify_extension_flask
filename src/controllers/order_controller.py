from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.OrderSchema import order_schema, orders_schema
from models.User import User
from models.Customer import Customer
from models.Order import Order
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta
from sqlalchemy import text


order = Blueprint("order", __name__, url_prefix="/order")


@order.route("/customer/<int:customer_id>", methods=["POST"])
@jwt_required
def new_order(customer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    # order_fields = order_schema.load(request.json)
    
    new_order = Order()
    # new_order.product = order_fields["product"]
    new_order.customer_id = customer_id

    user.order_id.append(new_order)
    
    customer = Customer.query.filter_by(customer_of=user.id, id = customer_id).first()
    
    customer.orders.append(new_order)
        
    db.session.add(new_order)
    db.session.commit()
        
    return jsonify(order_schema.dump(new_order))