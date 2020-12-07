from main import ma
from models.Customer import Customer
from marshmallow.validate import Length, Email

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

    email = ma.String(required=True, validate=[Length(min=4), Email()])

customer_schema = CustomerSchema()