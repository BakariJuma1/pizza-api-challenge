from server.app import db
from sqlalchemy_serializer import SerializerMixin


class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza")
 
