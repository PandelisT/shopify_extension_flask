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


@order.route("/", methods=["POST"])
@jwt_required
def new_order():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    order_fields = order_schema.load(request.json)
    
    new_order = Habit()
    new_order.habit = habit_fields["habit"]
    new_order.customer_id = habit_fields["customer_id"]

    user.habit_id.append(new_habit)

    customer = Customer.query.filter_by(customer_of=user.id, id = new_habit.customer_id).first()
    customer.habits.append(new_habit)
        
    db.session.add(new_habit)
    db.session.commit()
        
    return jsonify(habit_schema.dump(new_habit))