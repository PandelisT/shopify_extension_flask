from main import db
from flask import Blueprint
import os

db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")


@db_commands.cli.command("dump")
def dump_db():
    print("Dumping all database in database_dump file")
    os.system("""pg_dump -U postgres -W -d shopify_extension >
                ./database_dump.sql""")
    print("Dumped all database in database_dump file")


@db_commands.cli.command("seed")
def seed_db():
    from models.User import User
    from models.Customer import Customer
    from models.Product import Product
    from models.Order import Order
    from models.Article import Article
    from models.Habit import Habit
    from models.Tag import Tag
    from models.Note import Note
    from main import bcrypt

    users = []

    user = User()
    user.email = "test1@test.com"
    user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
    db.session.add(user)
    users.append(user)
    print(user)

    db.session.commit()

    customers = []

    for i in range(1, 11):
        customer = Customer()
        customer.fname = f"firstname{i}"
        customer.lname = f"lastname{i}"
        customer.email = f"name{i}@email.com"
        customer.customer_of = 1
        customer.is_active = True
        customers.append(customer)
        print(customer)

        db.session.add(customer)

    db.session.commit()

    for i in range(1, 21):
        product = Product()
        product.title = f"title{i}"
        product.description = f"description{i}"
        product.quantity = 1
        product.price = 10
        product.user_id = 1
        db.session.add(product)
        print(product)

    db.session.commit()

    for i in range(1, 21):
        article = Article()
        article.title = f"title{i}"
        article.body_html = f"Body text{i}"
        article.summary = f"Summary{i}"
        article.allow_comments = True
        article.custom_post_type = f"Custom Post Type{i}"
        article.show_date_and_author = True
        article.show_summary = True
        article.user_id = 1
        print(article)
        db.session.add(article)

    db.session.commit()

    for i in range(1, 11):
        habit = Habit()
        habit.habit = f"Habit number {i}"
        habit.user_id = 1
        print(habit)
        db.session.add(habit)

    db.session.commit()

    for i in range(1, 11):
        tag = Tag()
        tag.tag = f"Tag number {i}"
        tag.user_id = 1
        print(tag)
        db.session.add(tag)

    db.session.commit()

    for i in range(1, 11):
        order = Order()
        order.customer_id = i
        order.customer_of = 1
        print(order)
        db.session.add(order)

    db.session.commit()

    for i in range(1, 11):
        note = Note()
        note.note = f"Note number {i}"
        note.comms_type = "Email"
        note.user_id = 1
        note.customer_id = i
        print(note)
        db.session.add(note)

    db.session.commit()
