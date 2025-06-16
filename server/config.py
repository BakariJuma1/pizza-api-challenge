import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://userone:1234@localhost:5432/restaurantdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
