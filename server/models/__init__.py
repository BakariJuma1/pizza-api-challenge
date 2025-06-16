from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here to register them
from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza
