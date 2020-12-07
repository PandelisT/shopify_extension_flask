from main import ma
from models.Note import Note
from marshmallow.validate import Length, Email

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
    
    users = ma.Nested("UserSchema", many=True, only=("id", "username", "email"))
    items = ma.Nested("ItemSchema", many=True, exclude=("checklist_id",))


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)