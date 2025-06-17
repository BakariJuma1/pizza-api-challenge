# pizza-api-challenge
# 🍕 Pizza Restaurant API

A RESTful API for managing pizzas, restaurants, and their pricing using **Flask**, **SQLAlchemy**, and **Flask-Migrate**. This API allows users to view pizzas and restaurants, link pizzas to restaurants with prices, and perform CRUD operations.

---

## Project Structure

.
├── server/
│ ├── init.py
│ ├── app.py # App initialization
│ ├── config.py # DB configuration
│ ├── models/
│ │ ├── init.py
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── pizza_controller.py
│ │ ├── restaurant_controller.py
│ │ └── restaurant_pizza_controller.py
│ ├── seed.py # Seed file for testing data
├── migrations/ # Flask-Migrate files
├── challenge-1-pizzas.postman_collection.json
└── README.md

Copy
Edit

---

## 🧰 Tech Stack

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- PostgreSQL
- Postman (for API testing)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
2. Create a virtual environment and install dependencies
bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
3. Set environment variables
bash
Copy
Edit
export FLASK_APP=server/app.py
4. Run migrations
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Seed the database
bash
Copy
Edit
python server/seed.py
6. Run the Flask server
bash
Copy
Edit
flask run
 API Endpoints
🔹 GET /restaurants
Returns a list of all restaurants.

  Response:
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Mama's Pizza",
    "address": "123 Main Street"
  }
]
🔹 GET /restaurants/<int:id>
Returns a restaurant and the pizzas it offers.

 Success:
json
Copy
Edit
{
  "id": 1,
  "name": "Mama's Pizza",
  "address": "123 Main Street",
  "pizzas": [
    {
      "id": 2,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    }
  ]
}
 Error:
json
Copy
Edit
{ "error": "Restaurant not found" }
Status Code: 404 Not Found

🔹 DELETE /restaurants/<int:id>
Deletes a restaurant and all related restaurant-pizza entries.

  Response:
Status Code: 204 No Content

❌ Error:
json
Copy
Edit
{ "error": "Restaurant not found" }
Status Code: 404 Not Found

🔹 GET /pizzas
Returns a list of all available pizzas.

✅ Response:
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato, Cheese, Pepperoni"
  }
]
🔹 POST /restaurant_pizzas
Creates a new RestaurantPizza (linking a pizza to a restaurant with a price).

  Request:
json
Copy
Edit
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
  Response:
json
Copy
Edit
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato, Cheese, Pepperoni"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Palace",
    "address": "456 Side Street"
  }
}
❌ Validation Error:
json
Copy
Edit
{ "errors": ["Price must be between 1 and 30"] }
Status Code: 400 Bad Request

  Validations
price in RestaurantPizza must be between 1 and 30.

Deleting a restaurant also deletes associated restaurant-pizzas (via cascade).

 Postman Testing
Open Postman

Click Import

Upload challenge-1-pizzas.postman_collection.json

Run the saved requests to test each route

  Example Seed Data
Defined in server/seed.py:

Sample pizzas: Margherita, Pepperoni

Restaurants: Mama’s Pizza, Pizza Palace

Linked via RestaurantPizza with pricing

