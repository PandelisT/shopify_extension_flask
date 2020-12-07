from main import ma
from models.Tag import Tag
from marshmallow.validate import Length, Email

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)