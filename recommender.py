import pandas as pd

cars = pd.read_csv("cars_dataset.csv")

def recommend_cars(preferences):

    filtered = cars.copy()

    if preferences["type"]:
        filtered = filtered[filtered["Type"] == preferences["type"]]

    if preferences["fuel"]:
        filtered = filtered[filtered["Fuel"] == preferences["fuel"]]

    filtered = filtered[
        (filtered["Price"] <= preferences["budget"]) &
        (filtered["Seats"] >= preferences["seats"])
    ]

    filtered["Score"] = (
        filtered["Mileage"] * 0.4 +
        filtered["Safety"] * 20 +
        filtered["Seats"] * 5
    )

    recommendations = filtered.sort_values(
        by="Score",
        ascending=False
    )

    return recommendations.to_dict(orient="records")
