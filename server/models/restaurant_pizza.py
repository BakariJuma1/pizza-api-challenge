from server.app import db
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    
    restaurant = db.relationship("Restaurant", backref="restaurant_pizzas")
    pizza = db.relationship("Pizza", backref="restaurant_pizzas")

    def validate(self):
        return 1 <= self.price <= 30
