from flask import Blueprint, abort, jsonify, request
from schemas.HabitSchema import habit_schema, habits_schema
from models.User import User
from models.Customer import Customer
from models.Habit import Habit
from models.CustomersHabits import customers_habits
from main import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


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

    if new_habit.habit is None:
        return abort(400, "Need to add habit field")

    user.habit_id.append(new_habit)
    db.session.add(new_habit)
    db.session.commit()

    return jsonify(habit_schema.dump(new_habit))


@habit.route("/customer/<int:customer_id>/habit/<int:habit_id>",
             methods=["POST"])
@jwt_required
def new_habit_customer(customer_id, habit_id):
    # Adds a habit to a customer
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    customer = Customer.query.filter_by(customer_of=user.id,
                                        id=customer_id).first()
    habit = Habit.query.filter_by(id=habit_id).first()

    if not customer or not habit:
        return abort(404, "Customer or habit not found")

    customer.habits.append(habit)

    db.session.add(habit)
    db.session.commit()

    return jsonify(habit_schema.dump(habit))


@habit.route("/", methods=["GET"])
@jwt_required
def get_habits():
    # Gets all habits for user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    habits = [Habit.query.get(habit.id) for habit in user.habit_id]

    if habits == []:
        return "No habits for this user"

    return jsonify(habits_schema.dump(habits))


@habit.route("/customer/<int:customer_id>", methods=["GET"])
@jwt_required
def get_habits_for_customer(customer_id):
    # Gets all habits for customer of user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    habits = db.session.query(Habit).filter(
        customers_habits.c.customer_id == customer_id).all()

    if habits == []:
        return "No habits for this customer"

    return jsonify(habits_schema.dump(habits))


@habit.route("/<int:habit_id>", methods=["DELETE"])
@jwt_required
def delete_habit(habit_id):
    # Deletes habit for user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    habit = Habit.query.filter_by(id=habit_id).first()

    if not habit:
        return abort(404, description="Habit not found.")

    db.session.delete(habit)
    db.session.commit()

    return jsonify("The following habit was deleted from the database.",
                   habit_schema.dump(habit))


@habit.route("/<int:habit_id>", methods=["PUT"])
@jwt_required
def update_habit(habit_id):
    # Updates a habit for user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    habit_fields = habit_schema.load(request.json)
    habit = Habit.query.filter_by(id=habit_id)

    if habit.count() != 1:
        return abort(404, description="Habit not found.")

    habit.habit = habit_fields["habit"]

    habit.update(habit_fields)
    db.session.commit()

    return jsonify(habit_schema.dump(habit))
