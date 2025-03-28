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
    meals = Meal.query.all()
    if meals:
        meals_list = [{"id":m.id, "name":m.name, "description": m.description, "created_in": m.created_in, "diet": m.diet} for m in meals]
        output = {
           "meals" : meals_list
            }
        return jsonify(output)

    return jsonify({"message":"No meals registered"}), 404

@app.route('/meal/<int:id_meal>', methods=['GET'])
def read_meal(id_meal):
    meal = Meal.query.get(id_meal)
    if meal:
        status = "✓" if meal.diet == "1" else " "
        return jsonify({"message": f"({id_meal}). {meal.name}: {meal.description} / In diet [{status}] / created in: {meal.created_in}"})
    
    return jsonify({"message":"Meal not found"}), 404

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

@app.route('/meal/<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal):
   meal = Meal.query.get(id_meal)
   if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message":"Meal succesfully deleted"})
   
   return jsonify({"message":"Meal not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)