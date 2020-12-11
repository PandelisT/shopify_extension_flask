from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.CustomerSchema import customer_schema
from schemas.NoteSchema import note_schema, notes_schema
from models.User import User
from models.Customer import Customer
from models.Note import Note
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta


note = Blueprint("note", __name__, url_prefix="/note")


@note.route("/customer/<int:customer_id>", methods=["POST"])
@jwt_required
def new_note(customer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    note_fields = note_schema.load(request.json)
    
    new_note = Note()
    new_note.note = note_fields["note"]
    new_note.comms_type = note_fields["comms_type"]
    new_note.customer_id = customer_id

    user.note_id.append(new_note)
        
    db.session.add(new_note)
    db.session.commit()
        
    return jsonify(note_schema.dump(new_note))


@note.route("/<int:note_id>", methods=["GET"])
@jwt_required
def get_note():
    pass

@note.route("/<int:note_id>/customer/<int:customer_id>", methods=["GET"])
@jwt_required
def get_note_for_customer():
    pass

@note.route("/", methods=["GET"])
@jwt_required
def get_all_notes_for_user():
    pass

@note.route("/customer/<int:customer_id>", methods=["GET"])
@jwt_required
def get_all_notes_for_customer():
    pass

@note.route("/<int:note_id>", methods=["DELETE"])
@jwt_required
def delete_note():
    pass

@note.route("/<int:note_id>", methods=["PUT"])
@jwt_required
def update_note():
    pass