# Daily-Diet-API
from flask import Flask, request, jsonify
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"

db.init_app(app)

@app.route('/meal', methods=['POST'])
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    if name:
        meal = Meal(name=name, description=description, diet=True)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message":"Meal succesfully created"})

    return jsonify({"message":"Invalid data"}), 401

@app.route('/list', methods=['GET'])
def list_meals():
    pass

@app.route('/meal/<int:id_meal>', methods=['PUT'])
def update_meal(id_meal):
    data = request.json
    meal = Meal.query.get(id_meal)

    if meal:
        meal.name = data.get("name")
        meal.description = data.get("description")
        meal.created_in = data.get("created in (YYYY-MM-DD HH:MM)")
        meal.diet = data.get("diet")
        db.session.commit()
        return jsonify({"message":f"Meal {id_meal} succesfully updated"})

    return jsonify({"message":"Meal not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)