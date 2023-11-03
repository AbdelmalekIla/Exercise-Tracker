import requests


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

response = requests.post(url=nutritionix_url, json=nutritionix_body, headers=header_app)
print(response.text)


