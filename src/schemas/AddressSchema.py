from main import ma
from models.Address import Address


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address


address_schema = AddressSchema()
