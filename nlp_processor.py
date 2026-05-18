def extract_preferences(user_input):
    text = user_input.lower()

    preferences = {
        "budget": 1500000,
        "type": None,
        "fuel": None,
        "seats": 5
    }

    if "suv" in text:
        preferences["type"] = "SUV"

    if "sedan" in text:
        preferences["type"] = "Sedan"

    if "diesel" in text:
        preferences["fuel"] = "Diesel"

    if "petrol" in text:
        preferences["fuel"] = "Petrol"

    if "7 seater" in text:
        preferences["seats"] = 7

    return preferences
