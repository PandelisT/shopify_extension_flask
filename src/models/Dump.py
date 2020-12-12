from main import db
from datetime import datetime 
from sqlalchemy.orm import relationship
from sqlalchemy import text

class Dump(db.Model):
    __tablename__ = "dump"

    id = db.Column(db.Integer, primary_key=True)


    @classmethod
    def habit_dump(cls):
        sql_query = text("SELECT * FROM habits;")
        return  db.engine.execute(sql_query)



