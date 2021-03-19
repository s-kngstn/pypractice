from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary
        #Method 2 with dictionary comprehension
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafes = random.choice(cafes)
    return jsonify(cafe=random_cafes.to_dict())
    # return jsonify(cafe={
    #     "id": random_cafes.id,
    #     "name": random_cafes.name,
    #     "map_url": random_cafes.map_url,
    #     "img_url": random_cafes.img_url,
    #     "location": random_cafes.location,
    #     "seats": random_cafes.seats,
    #     "has_toilet": random_cafes.has_toilet,
    #     "has_wifi": random_cafes.has_wifi,
    #     "has_sockets": random_cafes.has_sockets,
    #     "can_take_calls": random_cafes.can_take_calls,
    #     "coffee_price": random_cafes.coffee_price,
    # }
    # )
# GET ALL
@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    
# FIND A CAFE
@app.route("/search")
def get_cafe_at_location():
    find_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=find_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
