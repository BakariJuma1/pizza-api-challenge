from flask import Blueprint, request, jsonify
from server.models import db, RestaurantPizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    # Your route logic here
    return jsonify({"message": "Created!"}), 201
