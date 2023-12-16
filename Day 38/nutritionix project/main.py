# https://requests.readthedocs.io/en/latest/api/
# https://developer.syndigo.com/docs/nutritionix-api-guide
# https://developer.nutritionix.com/
import requests
import datetime
import os

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 1.69
AGE = 27


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ['SHEET_ENDPOINT']

nutritionix_headers = {
    "x-app-id": os.environ['NT_APP_ID'],
    "x-app-key": os.environ['NT_API_KEY'],
}

exercise_text = input("Tell me which exercises you did: ")

nutritionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=nutritionix_params, headers=nutritionix_headers)
result = response.json()
calories = result['exercises'][0]['nf_calories']
duration = result['exercises'][0]['duration_min'] / 60
exercise_name = result['exercises'][0]['name']

# Saving data into google sheet
# https://sheety.co/
# https://sheety.co/docs/authentication.html
# https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication
# https://docs.google.com/spreadsheets/d/12KaV8lhBTp5YeCpxqkOMha99Hlio57c4cla8Jw-qFpg/edit#gid=0

today = datetime.datetime.now()

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

sheet_params = {
    "workout":
        {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise_name.title(),
            "duration": duration,
            "calories": calories,
        }
}

response = requests.post(url=sheet_endpoint, json=sheet_params, headers=bearer_headers)
print(response.text)
