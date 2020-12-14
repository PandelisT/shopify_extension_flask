from main import db


customers_habits = db.Table("customers_habits", db.Model.metadata,
                            db.Column("customer_id", db.Integer,
                                      db.ForeignKey("customers.id")),
                            db.Column("habit_id", db.Integer,
                                      db.ForeignKey("habits.id")))
