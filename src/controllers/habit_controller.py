from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.HabitSchema import habit_schema, habits_schema
from models.User import User
from models.Customer import Customer
from models.Habit import Habit
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta
from sqlalchemy import text


habit = Blueprint("habit", __name__, url_prefix="/habit")


@habit.route("/", methods=["POST"])
@jwt_required
def new_habit():
    # Adds a new habit to the database
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    habit_fields = habit_schema.load(request.json)
    
    new_habit = Habit()
    new_habit.habit = habit_fields["habit"]

    user.habit_id.append(new_habit)
        
    db.session.add(new_habit)
    db.session.commit()
        
    return jsonify(habit_schema.dump(new_habit))

@habit.route("/customer/<int:customer_id>/habit/<int:habit_id>", methods=["POST"])
@jwt_required
def new_habit_customer(customer_id, habit_id):
    # Adds a habit to a customer
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    customer = Customer.query.filter_by(customer_of=user.id, id = customer_id).first()
    habit = Habit.query.filter_by(id = habit_id).first()
    print(habit.habit)
    customer.habits.append(habit)
        
    db.session.add(habit)
    db.session.commit()
        
    return jsonify(habit_schema.dump(habit))


@habit.route("/", methods=["GET"])
@jwt_required
def get_user_checklists():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    habits = [Habit.query.get(habit.id) for habit in user.habit_id]

    return jsonify(habits_schema.dump(habits))


@habit.route("/<int:customer_id>", methods=["GET"])
@jwt_required
def checklist_get(customer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    result = Habit.habit_filter(customer_id, user.id)
    result_as_list = result.fetchall()

    habit_list = []
    for habit in result_as_list:
        habit_list.append({"id": habit.id, "habit": habit.habit})

    return jsonify(habit_list)


@habit.route("/<int:habit_id>", methods=["DELETE"])
@jwt_required
def delete_habit():
    pass

@habit.route("/<int:habit_id>", methods=["PUT"])
@jwt_required
def update_habit():
    pass