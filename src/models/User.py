from main import db
from models.Customer import Customer
from models.Note import Note 
from models.Tag import Tag
from models.Habit import Habit
from models.Order import Order
from models.Product import Product
from models.Article import Article

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    customer_id = db.relationship(Customer, backref="user", uselist=True)
    note_id = db.relationship(Note, backref="user", uselist=True)
    tag_id = db.relationship(Tag, backref="user", uselist=True)
    habit_id = db.relationship(Habit, backref="user", uselist=True)
    order_id =  db.relationship(Order, backref="user", uselist=True)
    product_id = db.relationship(Product, backref="user", uselist=True)
    article_id = db.relationship(Article, backref="user", uselist=True)
    
    def __repr__(self):
        return f"<User {self.email}>"