from datetime import datetime 
from sqlalchemy.orm import relationship


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    body_html = db.Column(db.String(), nullable=False)
    summary = db.Column(db.String(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    allow_comments = db.Column(db.Boolean, default=True)
    custom_post_type = db.Column(db.String)
    show_date_and_author = db.Column(db.Boolean, default=True)
    show_summary = db.Column(db.Boolean, default=True)


    def __repr__(self):
        return f"<Article {self.title}>"