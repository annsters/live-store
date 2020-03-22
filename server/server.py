from flask import (Flask, request, abort, jsonify)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
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

db.create_all()

items = []
@app.route("/")
def hello():
    return "hello"

# @app.route("/search", methods = ["POST"])
# def newSearch():
@app.route("/newItem", methods = ["POST"])
def postItem():

    print("postinglkaj")
    print(request.json)
    item = request.json.get('name', None)

   

    items.append(item)
    print(items)
    print("Succesfully added item")

    return jsonify(),200

if __name__ == '__main__':
    app.run(debug = True)

