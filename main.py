import requests
import datetime as dt

time = dt.datetime.now()
date_now = time.strftime("%d/%m/%Y")
time_h_now = time.strftime("%I:%M:%S")
sheet_app_api = "https://api.sheety.co/eef2f21b5cd52c5e74271578b4600a55/workoutTracking/workouts"
new_row = "https://api.sheety.co/phill/myWebsite/emails"
nutritionix_application_id = "ed341e25"
nutritionix_apikey = "7726a49a2d43c7f62405079773ef5f7d"  # 45ccdff66bdbf9c9746ae9b3504658eb
header_app = {
    "x-app-key": nutritionix_apikey,
    "x-app-id": nutritionix_application_id
}

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
new_row_pi = {
    "workout": {
        "date": date_now,
        "time": time_h_now,
    }
}

# response = requests.post(url=nutritionix_url, json=nutritionix_body, headers=header_app)
# data = response.json()["exercises"]
# print(response.text)

insert_data = requests.post(url=sheet_app_api, json=new_row_pi)
print(insert_data)
# workout_data = {i for i in data if i == "user_input"}
# print(workout_data)
