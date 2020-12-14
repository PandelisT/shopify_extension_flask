from main import db
from datetime import datetime
from models.CustomersHabits import customers_habits
from sqlalchemy import text


class Habit(db.Model):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)
    habit = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                        nullable=False)
    customers = db.relationship("Customer", secondary=customers_habits,
                                back_populates="habits")

    @classmethod
    def habit_filter(cls, customer_id, user_id):
        sql_query = text("""SELECT * FROM  habits WHERE customer_id =
                         ':customer_id' and user_id=':user_id';""")
        return db.engine.execute(sql_query, {"customer_id": customer_id,
                                 "user_id": user_id})

    def __repr__(self):
        return f"<Habit {self.id}>"
