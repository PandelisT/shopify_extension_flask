from flask import Blueprint, abort, jsonify, request
from schemas.DumpSchema import dump_schema
from models.Dump import Dump
from models.User import User
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import text
from datetime import timedelta
from flask_alchemydumps import AlchemyDumps


admin = Blueprint("admin", __name__, url_prefix="/admin/dump")


@admin.route("/", methods=["POST"])
@jwt_required
def dump_all():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    # dump = Dump.habit_dump().all()
    sql_query = text("SELECT * FROM habits;")
    return  db.engine.execute(sql_query)

    # print(dump)
        
    # return jsonify(dumps_schema.dump(dump))