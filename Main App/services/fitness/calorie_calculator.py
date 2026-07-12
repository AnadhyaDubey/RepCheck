MET_VALUES = {
    "Squats": 5.0,
    "Push-ups": 8.0,
    "Biceps Curls (Dumbbell)": 3.5,
    "Shoulder Press": 4.0,
    "Lunges": 4.5,
}

def calculate_calories(exercise: str, duration_seconds: float, weight_kg: float) -> float:
    met = MET_VALUES.get(exercise, 4.0)
    duration_hours = duration_seconds / 3600
    calories = met * weight_kg * duration_hours
    return round(calories, 1)