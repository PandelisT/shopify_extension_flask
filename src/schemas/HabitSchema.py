from main import ma
from models.Habit import Habit

class HabitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Habit
    
    customer = ma.Nested("CustomerSchema", many=True)


habit_schema = HabitSchema()
habits_schema = HabitSchema(many=True)