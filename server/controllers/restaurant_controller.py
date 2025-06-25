from flask import Blueprint,jsonify,request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.models import db


restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

# @restaurant_bp.route('/restaurant', methods=['GET'])
# def index():
#     return {"message": "Restaurant route working"}

@restaurant_bp.route("/", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [r.to_dict() for r in restaurants]
    return jsonify(result), 200


@restaurant_bp.route("/<int:id>", methods=["GET"])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    data = restaurant.to_dict(rules=('restaurant_pizzas.pizza',)) 
    return jsonify(data), 200


@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204