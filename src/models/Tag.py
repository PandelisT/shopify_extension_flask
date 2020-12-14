from main import db
from datetime import datetime
from models.CustomersTags import customers_tags


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                        nullable=False)
    customers = db.relationship("Customer", secondary=customers_tags,
                                back_populates="tags")

    def __repr__(self):
        return f"<Tag {self.id}>"
