import requests
import datetime as dt
import os

# Adding date and time
time = dt.datetime.now()
date_now = time.strftime("%d/%m/%Y")
time_h_now = time.strftime("%X")

# Sheet Auth
MY_AUTH = os.environ["MY_AUTH"]
sheet_app_api = os.environ['SHEET_APP_API']

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
nutritionix_application_id = os.environ['NUTRITIONIX_APPLICATION_ID']
nutritionix_apikey = os.environ['NUTRITIONIX_APIKEY']

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Nutritionix API Call
header_app = {
    "x-app-key": nutritionix_apikey,
    "x-app-id": nutritionix_application_id
}

sheet_header = {
    "Authorization": f"Basic {MY_AUTH}"
}

nutritionix_body = {
    "query": input("tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 51,
    "height_cm": 190.0,
    "age": 22
}
sheet_body = {
    "Date": date_now,
    "Time": time_h_now,

}

response = requests.post(url=nutritionix_url, json=nutritionix_body, headers=header_app)
data = response.json()["exercises"]
workout_data = [{"name": item["name"], "duration_min": item["duration_min"], "nf_calories": item["nf_calories"]} for item in data]


for exercise in workout_data:
    new_row_pi = {
        "workout": {
            "date": date_now,
            "time": time_h_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    send_to_sheet = requests.post(url=sheet_app_api, json=new_row_pi, headers=sheet_header)







