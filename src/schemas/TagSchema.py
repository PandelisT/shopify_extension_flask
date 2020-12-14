from main import ma
from models.Tag import Tag


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag

    customer = ma.Nested("CustomerSchema", many=True)


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
