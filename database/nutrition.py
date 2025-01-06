def get_nutrition_info(food_item):
    # Dummy data (replace with real database/API logic)
    nutrition_data = {
        "apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
        "banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23},
    }
    return nutrition_data.get(food_item.lower(), "Food item not found.")
