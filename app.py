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
        return jsonify({"message":"Meal succesfully updated"})

    return jsonify({"message":"Invalid data"}), 401

@app.route('/list', methods=['GET'])
def list_meals():
    pass


if __name__ == "__main__":
    app.run(debug=True)