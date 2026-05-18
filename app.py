from flask import Flask, request, jsonify
from flask_cors import CORS

from nlp_processor import extract_preferences
from recommender import recommend_cars
from emi_calculator import calculate_emi
from fuel_cost import calculate_fuel_cost
from ownership_cost import calculate_ownership_cost

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.json
    user_query = data["query"]

    preferences = extract_preferences(user_query)

    recommendations = recommend_cars(preferences)

    return jsonify(recommendations)

@app.route("/emi", methods=["POST"])
def emi():

    data = request.json

    emi = calculate_emi(
        data["price"],
        data["interest"],
        data["years"]
    )

    return jsonify({"emi": emi})

@app.route("/fuel", methods=["POST"])
def fuel():

    data = request.json

    cost = calculate_fuel_cost(
        data["distance"],
        data["mileage"],
        data["fuel_price"]
    )

    return jsonify({"fuel_cost": cost})

@app.route("/ownership", methods=["POST"])
def ownership():

    data = request.json

    total = calculate_ownership_cost(
        data["price"],
        data["maintenance"],
        data["fuel_cost"]
    )

    return jsonify({"ownership_cost": total})

if __name__ == "__main__":
    app.run(debug=True)
