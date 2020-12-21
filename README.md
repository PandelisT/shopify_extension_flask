# Shopify API extension

## Description

This Flask REST API is an extension to the SHopify REST API found here: https://shopify.dev/docs/admin-api/rest/reference.

The extension includes the addition of new tables and relationships including adding tags, habits and notes to customers and connecting products with blog posts.

The endpoints for this project can be found in openapi.yml.

## Instructions

The instructions for Ubuntu 20:

Update repositories on Ubuntu: ```sudo apt-get update```

Clone GitHub repository: ```git clone https://github.com/PandelisT/shopify_extension_flask.git ```

Install python virtual environment: ```sudo apt-get install python3.8-venv```

Create virtual environment: ```python3.8 -m venv venv```

Activate the virtual environment ```source venv/bin/activate```

Install pip: ```python -m pip install --upgrade pip```

Install modules from requirements.txt: ```pip install -r requirements.txt```

**To seed the database, run the following commands:**

```flask db-custom drop``` (If there are any tables in the database previously)

```flask db upgrade``` (to add the tables in the migrations directory)

```flask db-custom seed``` (to seed the database)

```flask db-custom dump``` (to dump the database into the database_dump.sql file. The user must be 'postgres' for this to work)

Dumping all the data can also be achieved by running this endpoint:```customer/dump``` with the token for the specific user. 

Note: seeding includes populating these tables:

1. Users (for simplicity populated with 1 user which will have many customers, products, habits, tags, orders and notes for customers),
2. 5 customers in Customers,
3. 20 products in Products,
4. 20 articles in articles,
5. 10 habits in Habits,
6. 10 tags in Tags,
7. 10 orders in Orders,
8. 10 notes in Notes.

The association of products with orders has to be made with the endpoint:

```/product/{product_id}/order/{order_id}```

Habits and tags also need to be associated with specific customers with the endpoints:

```/tag/customer/{customer_id/tag_id/{tag_id}```
```/habit/customer/{customer_id}/habit/{habit_id}```

The full list of API endpoints can be found in the swagger.yml file.

The front end consists of only one end point ```/customer/user/1``` which show a list of customers.

To connect to the database locally, please fill in the .env file like this example:
FLASK_APP=src/main.py
FLASK_ENV=development
DB_USER = postgres
DB_PASSWORD = postgres
DB_HOST = localhost:5432
DB_NAME = shopify_extension
JWT_SECRET_KEY = "duck"
AWS_ACCESS_KEY_ID=1
AWS_SECRET_ACCESS_KEY=1
AWS_S3_BUCKET=1