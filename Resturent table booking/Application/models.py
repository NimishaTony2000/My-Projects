from email.policy import default
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class Registraion(db.Model,UserMixin):     
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    email=db.Column(db.String(50))
    address=db.Column(db.String(50))
    password=db.Column(db.String(50))


class Restaurant(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    
    name=db.Column(db.String(100))
    location=db.Column(db.String(100))
    about=db.Column(db.String(600))

class Login(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))
    user_type=db.Column(db.String(40))

class Table(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    restaurant_id=db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    booked_status=db.Column(db.String(100))
    no_of_chairs=db.Column(db.String(100))
    

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    login_id=db.Column(db.Integer,db.ForeignKey('login.id'))
    name=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    mail=db.Column(db.String(100))

class Reservation(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    table_id=db.Column(db.Integer,db.ForeignKey('table.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    payment_amount=db.Column(db.String(100))

