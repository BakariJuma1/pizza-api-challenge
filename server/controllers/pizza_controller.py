from flask import Blueprint, request, jsonify
from server.models import db, Pizza


pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [p.to_dict() for p in pizzas]
    return jsonify(result)
