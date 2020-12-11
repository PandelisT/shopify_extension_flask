from main import db
from datetime import datetime
from sqlalchemy.orm import relationship
from models.CustomersTags import customers_tags
from sqlalchemy import text


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    customers = db.relationship("Customer", secondary=customers_tags, back_populates="tags")


    @classmethod
    def tag_filter(cls, customer_id):
        sql_query = text("SELECT * FROM  customers_tags WHERE customer_id = ':customer_id';")
        return db.engine.execute(sql_query, {"customer_id": customer_id})

    def __repr__(self):
        return f"<Tag {self.id}>"