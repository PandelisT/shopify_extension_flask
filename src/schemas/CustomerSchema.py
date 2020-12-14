from main import ma
from models.Customer import Customer
from marshmallow.validate import Length, Email


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

    email = ma.String(required=True, validate=[Length(min=4), Email()])
    habits = ma.Nested("HabitSchema", many=True)
    tags = ma.Nested("TagSchema", many=True)
    notes = ma.Nested("NoteSchema", many=True)
    orders = ma.Nested("OrderSchema", many=True)
    address = ma.Nested("AddressSchema")


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
