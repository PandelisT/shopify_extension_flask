from main import ma
from models.Note import Note
from marshmallow.validate import Length, Email

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
    

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)