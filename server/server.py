from flask import (Flask, request, abort)
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://annielu:blizzard@localhost/store-db'
db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    category = db.Column(db.String(120))
    amount = db.Column(db.String(120))
   

    def __init__(self, user, item, store, location):
        self.name = name
        self.category = category
        self.amount = amount

class Stores(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    location = db.Column(db.String(120))
    

    def __init__(self, user, item, store, location):
        self.name = name
        self.location = location


items = []
@app.route("/")
def hello():
    return "hello"

# @app.route("/search", methods = ["POST"])
# def newSearch():
@app.route("/newitem", methods = ["POST"])

def postItem():
    item = request.json['item']
    items.append(item)
    return "Succesfully added item"

if __name__ == '__main__':
    app.run(debug = True)

