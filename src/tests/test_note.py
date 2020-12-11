import unittest
from main import create_app, db
from flask import Blueprint, abort, jsonify, request
from models.User import User
from models.Note import Note
from schemas.CustomerSchema import customer_schema
from models.Customer import Customer
from flask_jwt_extended import create_access_token
import random

class TestAuth(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])
        print("setup ran")

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
        print("teardown ran")

    def test_get_note(self):
        note = random.choice(Note.query.all())
        user = User.query.get(note.user_id)
        access_token = create_access_token(identity=str(user.id))
        response = self.client.get("/note/", headers={ "Authorization": f"Bearer {access_token}"})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    # def test_note_post(self):
    #     user = random.choice(User.query.all())
    #     customer_fields = customer_schema.load(request.json)
    
    #     new_customer = Customer()
    #     new_customer.fname = customer_fields["fname"]
    #     new_customer.lname = customer_fields["lname"]
    #     new_customer.email = customer_fields["email"]
    #     new_customer.is_active= customer_fields["is_active"]

    #     user.customer_id.append(new_customer)
        
    #     db.session.add(new_customer)

    #     customer_id = Customer.query.filter_by(customer_of=user.id).first()
        
    #     print(user)
    #     print(customer_id)
    #     access_token = create_access_token(identity=str(user.id))
    #     response = self.client.post(f"/note/customer/{customer_id}", json={"note": "test habit", "comms_type" : "Email"}, headers={ "Authorization": f"Bearer {access_token}"})
    #     data = response.get_json()

    #     self.assertEqual(response.status_code, 200)