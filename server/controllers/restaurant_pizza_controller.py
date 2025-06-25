from flask import Blueprint, request, jsonify
from server.models import db, RestaurantPizza,Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/pizzas')
def get_pizzas():
    pizzas = Pizza.query.all()
    # print(pizzas)

    return jsonify([pizza.to_dict() for pizza in pizzas])



@restaurant_pizza_bp.route("/restaurant_pizza", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data["price"])
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]
    except (KeyError, ValueError, TypeError):
        return jsonify({"errors": ["Invalid input"]}), 400

    if price < 1 or price > 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid restaurant or pizza ID"]}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify(rp.to_dict(rules=('pizza','restaurant'))), 201
