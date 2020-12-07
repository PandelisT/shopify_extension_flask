from main import ma
from models.User import User
from marshmallow.validate import Length, Email

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["password"]

    email = ma.String(required=True, validate=[Length(min=4), Email()])
    password = ma.String(required=True, validate=Length(min=6))
    tag_id =  ma.Nested("TagSchema", many=True)
    habit_id = ma.Nested("HabitSchema", many=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)