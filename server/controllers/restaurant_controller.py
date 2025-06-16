from flask import Blueprint

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def index():
    return {"message": "Restaurant route working"}
