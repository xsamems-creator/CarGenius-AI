def calculate_ownership_cost(
    price,
    yearly_maintenance,
    fuel_cost,
    years=5
):

    total = (
        price +
        (yearly_maintenance * years) +
        (fuel_cost * 12 * years)
    )

    return round(total, 2)
