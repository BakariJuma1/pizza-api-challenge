from server.models import db, Restaurant, Pizza
from server.app import create_app
from server.app import db
#  app instance
app = create_app()

#  app context
with app.app_context():
    print("Dropping all tables...")
    db.drop_all()

    print("Creating all tables...")
    db.create_all()

    print("Seeding data...")

    #  seed data 
    r1 = Restaurant(name="Mama's Pizza", address="123 Cheese Street")
    r2 = Restaurant(name="Pepperoni Palace", address="456 Tomato Ave")

    p1 = Pizza(name="Margherita", ingredients="Cheese, Tomato, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Cheese, Tomato, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    print(" Done seeding!")
