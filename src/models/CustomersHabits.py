from main import db

# The association table for the many to many relationship between customers and habits
customers_habits = db.Table("customers_habits", db.Model.metadata,
db.Column("customer_id", db.Integer, db.ForeignKey("customers.id")),
db.Column("habit_id", db.Integer, db.ForeignKey("habits.id"))
)