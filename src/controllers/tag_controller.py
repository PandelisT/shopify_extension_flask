from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.CustomerSchema import customer_schema
from schemas.TagSchema import tag_schema, tags_schema
from models.User import User
from models.Customer import Customer
from models.Tag import Tag
from models.CustomersTags import customers_tags
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta


tag = Blueprint("tag", __name__, url_prefix="/tag")


@tag.route("/", methods=["POST"])
@jwt_required
def new_tag():
    # Adds a new tag to the database
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    tag_fields = tag_schema.load(request.json)
    
    new_tag = Tag()
    new_tag.tag = tag_fields["tag"]
    new_tag.customer_id = 0

    user.tag_id.append(new_tag)
        
    db.session.add(new_tag)
    db.session.commit()
        
    return jsonify(tag_schema.dump(new_tag))

@tag.route("/customer/<int:customer_id>/tag_id/<int:tag_id>", methods=["POST"])
@jwt_required
def new_tag_customer(customer_id, tag_id):
    # Adds a tag to a customer
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    customer = Customer.query.filter_by(customer_of=user.id, id = customer_id).first()
    tag = Tag.query.filter_by(id = tag_id).first()
    customer.tags.append(tag)
        
    db.session.add(tag)
    db.session.commit()
        
    return jsonify(tag_schema.dump(tag))

@tag.route("/<int:tag_id>", methods=["GET"])
@jwt_required
def get_tag(tag_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    tag = Tag.query.filter_by(user_id = user.id).first()
        
    return jsonify(tag_schema.dump(tag))

@tag.route("/customer/<int:customer_id>", methods=["GET"])
@jwt_required
def get_tags_for_customer(customer_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    result = Tag.tag_filter(customer_id)
    result_as_list = result.fetchall()

    tag_list = []
    for tag in result_as_list:
        tag_id = tag[1]
        tag_list.append(tag_id)

    # tags = db.session.query(Tag).join(customers_tags).filter(customers_tags.customer_id == customer_id).all()

    return jsonify(tags_schema.dump(tag_list))

@tag.route("/", methods=["GET"])
@jwt_required
def get_all_tags_for_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    tags = Tag.query.filter_by(user_id = user.id).all()
        
    return jsonify(tags_schema.dump(tags))

@tag.route("/<int:tag_id>", methods=["DELETE"])
@jwt_required
def delete_tag(tag_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    tag = Tag.query.filter_by(id = tag_id).first()
    
    db.session.delete(tag)
    db.session.commit()
        
    return jsonify(tag_schema.dump(tag))

@tag.route("/<int:tag_id>", methods=["PUT"])
@jwt_required
def update_tag(tag_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    tag_fields = tag_schema.load(request.json)
    
    tag = Tag.query.filter_by(id = tag_id)
    tag.tag = tag_fields["tag"]

    return jsonify(tag_schema.dump(tag))
