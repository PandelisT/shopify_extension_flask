from main import ma
from models.CustomersTags import CustomersTags


class CustomersTagsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomersTags

customer_tags_schema = CustomerTagSchema()
customers__tags_schema = CustomerTagSchema(many=True)