# Django Product Management API

A Django REST Framework project with READ and WRITE endpoints for managing products, using Snowflake as the database backend.

## Setup Instructions

1. **Clone the repository** :
   ```bash
   git clone https://github.com/Meghshyams/django-product-management-snowflake.git
   cd snowflake

2. **Create a virtual environment** :
    ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies** :
   ```
   pip install -r requirements.txt

5. **Configure Snowflake** :
Create a .env file in the project root with your Snowflake credentials:
   ```bash
   SNOWFLAKE_USER=your_username
   SNOWFLAKE_PASSWORD=your_password
   SNOWFLAKE_ACCOUNT=your_account
   SNOWFLAKE_DATABASE=your_database
   SNOWFLAKE_SCHEMA=your_schema
   SNOWFLAKE_ROLE=your_role


6. **Run the server** :
   ```
   python manage.py runserver

7. **Requirements**
   - Python 3.8+
   - Snowflake account
      - Create Table

         CREATE TABLE products (
         product_id INTEGER AUTOINCREMENT,
         product_name VARCHAR(100),
         price DECIMAL(10, 2),
         quantity INTEGER,
         PRIMARY KEY (product_id)
      );

      INSERT INTO products (product_name, price, quantity) VALUES
      ('Laptop', 1200.00, 50),
      ('Mouse', 25.00, 200),
      ('Keyboard', 50.00, 150),
      ('Monitor', 300.00, 80);

   - Dependencies listed in requirements.txt


8. **Read Endpoint**
   ```
   curl -X GET http://127.0.0.1:8000/api/products/
```
Output :
```
[
    {"product_id": 1, "product_name": "Laptop", "price": 1200.0, "quantity": 50},
    {"product_id": 2 Pearson, "product_name": "Mouse", "price": 25.0, "quantity": 200},
    {"product_id": 3, "product_name": "Keyboard", "price": 50.0, "quantity": 150},
    {"product_id": 4, "product_name": "Monitor", "price": 300.0, "quantity": 80}
]
```
9. **Write Endpoint**
```
curl -X POST http://127.0.0.1:8000/api/products/ \
-H "Content-Type: application/json" \
-d '{"product_name": "Headphones", "price": 100, "quantity": 120}'

```
Output :
```
{"product_name": "Headphones", "price": 100, "quantity": 120}

10. Output Screenshots


