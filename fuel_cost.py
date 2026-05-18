def calculate_fuel_cost(
    monthly_distance,
    mileage,
    fuel_price
):
    liters_needed = monthly_distance / mileage
    cost = liters_needed * fuel_price

    return round(cost, 2)
