from flask import Blueprint, abort, jsonify, request
from schemas.NoteSchema import note_schema, notes_schema
from models.User import User
from models.Note import Note
from main import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


note = Blueprint("note", __name__, url_prefix="/note")


@note.route("/customer/<int:customer_id>", methods=["POST"])
@jwt_required
def new_note(customer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    note_fields = note_schema.load(request.json)

    try:
        new_note = Note()
        new_note.note = note_fields["note"]
        new_note.comms_type = note_fields["comms_type"]
        new_note.customer_id = customer_id
        user.note_id.append(new_note)
        db.session.add(new_note)
        db.session.commit()

        return jsonify(note_schema.dump(new_note))

    except Exception:
        return abort(400, description="Missing one or more fields")


@note.route("/<int:note_id>", methods=["GET"])
@jwt_required
def get_note(note_id):
    # Get note for user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    note = Note.query.filter_by(id=note_id).first()

    if note == {}:
        return abort(401, description="Invalid note")

    return jsonify(note_schema.dump(note))


@note.route("/<int:note_id>/customer/<int:customer_id>", methods=["GET"])
@jwt_required
def get_note_for_customer(note_id, customer_id):
    # Get note for customer of logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    note = Note.query.filter_by(id=note_id,
                                customer_id=customer_id).first()

    if note == []:
        return abort(403, description="No notes")

    return jsonify(note_schema.dump(note))


@note.route("/", methods=["GET"])
@jwt_required
def get_all_notes_for_user():
    # Get all notes for logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    notes = Note.query.filter_by(user_id=user.id).all()

    return jsonify(notes_schema.dump(notes))


@note.route("/customer/<int:customer_id>", methods=["GET"])
@jwt_required
def get_all_notes_for_customer(customer_id):
    # Get all notes for customer of logged in user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    notes = Note.query.filter_by(customer_id=customer_id).all()

    if notes == []:
        return abort(401,
                     description="Invalid customer or no note for customer")

    return jsonify(notes_schema.dump(notes))


@note.route("/<int:note_id>", methods=["DELETE"])
@jwt_required
def delete_note(note_id):
    # Delete note
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    note = Note.query.filter_by(id=note_id).first()

    if not note:
        return abort(401, description="Invalid note")

    db.session.delete(note)
    db.session.commit()

    return jsonify(note_schema.dump(note))


@note.route("/<int:note_id>", methods=["PUT"])
@jwt_required
def update_note(note_id):
    # Update note
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    note_fields = note_schema.load(request.json)
    note = Note.query.filter_by(id=note_id)

    if note.count() != 1:
        return abort(404, description="Not a valid note")

    note.note = note_fields["note"]
    note.comms_type = note_fields["comms_type"]
    note.update(note_fields)
    db.session.commit()

    return jsonify(note_schema.dump(note))
