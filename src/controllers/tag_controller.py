from flask import Blueprint, abort, jsonify, request
from schemas.UserSchema import user_schema
from schemas.CustomerSchema import customer_schema
from schemas.TagSchema import tag_schema, tags_schema
from models.User import User
from models.Customer import Customer
from models.Tag import Tag
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta


tag = Blueprint("tag", __name__, url_prefix="/tag")


@tag.route("/", methods=["POST"])
@jwt_required
def new_account():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    tag_fields = tag_schema.load(request.json)
    
    new_tag = Tag()
    new_tag.tag = tag_fields["tag"]
    new_tag.customer_id = tag_fields["customer_id"]

    user.tag_id.append(new_tag)
        
    db.session.add(new_tag)
    db.session.commit()
        
    return jsonify(tag_schema.dump(new_tag))