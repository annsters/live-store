from flask import (Flask, request, abort, jsonify)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost/store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storeId = db.Column('storeId', db.Integer)
    name = db.Column('name', db.String(80))
    category = db.Column('category',db.String(120))
    amount = db.Column('amount',db.Integer)
   

    def __init__(self, name, category, amount, storeId):
        self.name = name
        self.category = category
        self.amount = amount
        self.storeId = storeId

class Stores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storeName = db.Column('storeName', db.String(80), unique = True)
    latitude = db.Column('latitude', db.Float)
    longitude = db.Column('longitude', db.Float)
    category = db.Column('category', db.String(80))

    def __init__(self, storeName, category, latitude, longitude):
        self.storeName = storeName
        self.latitude = latitude
        self.longitude = longitude
        self.category = category

# is this bad on repeated invocations?
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

    newItem = Items(name=request.json.get('name'), category = request.json.get('category'), 
            amount = request.json.get('amount'), storeId = request.json.get('storeId'))
    
    db.session.add(newItem)
    db.session.flush()
    db.session.commit()

    return jsonify(),200

@app.route("/newStore", methods = ["POST"])
def postStore():

    print("posting store")
    print(request.json)
   

    newStore = Stores(storeName=request.json.get('storeName'), category = request.json.get('category'), 
            latitude = request.json.get('latitude'), longitude = request.json.get('longitude'))
    
    db.session.add(newStore)
    db.session.flush()
    db.session.commit()

    return jsonify(),200

if __name__ == '__main__':
    app.run(debug = True)

