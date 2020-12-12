from main import ma
from models.Dump import Dump

class DumpSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dump
    

dump_schema = DumpSchema()
dumps_schema = DumpSchema(many=True)