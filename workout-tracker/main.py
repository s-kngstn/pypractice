import os
import requests
from datetime import datetime

today = datetime.now()

APP_ID = "95f14dd2"
API_KEY = "efed37ab448605c3a4309c999f64c5a5"

WEIGHT_KG = 65.77089
HEIGHT_CM = 175.26
GENDER = "male"
AGE = 35

Nutritionix_Exercise_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

calc_exercise = input("Tell us which exercise you did: ")

nutritionix_config = {
    "query": calc_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}


response = requests.post(url=Nutritionix_Exercise_Endpoint, json=nutritionix_config, headers=headers)
exercise_data = response.json()["exercises"][0]
duration = exercise_data["duration_min"]
calories = exercise_data["nf_calories"]
exercise = exercise_data["name"]

username = "5bfbc5d944fbd9bebc73be327905bd56"
Sheety_Endpoint = f"https://api.sheety.co/{username}/workoutTracking/workouts"

headers = {"Authorization": "Bearer alfnmlfnl@#nDK129#@mdo(0olks32&6^2!!0d#76xnme"}

sheety_config = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
} 

add_exercise_data = requests.post(url=Sheety_Endpoint, json=sheety_config, headers=headers)
print(add_exercise_data.text)