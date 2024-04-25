import requests
import datetime
import time
API_ID = "0df663b9"
API_KEY = "9789e33d5886707bab8e1a892e5ab19b"
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_url = "https://api.sheety.co/b28fcec91afb2fa755e5e2e7484b8495/workoutTracking/workouts"
SHEET_NAME = "myWorkouts"

ticks = time.time()

headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
    "Content-Type": "application/json"
}

parameters = {
 "query":input("Tell me what exercise you did: "),
}

response = requests.post(url=url, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

now = datetime.datetime.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime("%H:%M:%S")
for i in result["exercises"]:
    exercise = i["name"]
    duration = i["duration_min"]
    calories = i["nf_calories"]

    sheet_header = {
        "Authorization": "Basic Y2xpbnQ6a2luZ3pvbGV4",
        "Content-Type" : "application/json"
    }
    data = { "workout" : {
     "date": str(date),
     "time": time,
     "exercise": exercise.title(),
     "duration": duration,
     "calories": calories
    }
    }
    rest = requests.post(url='https://api.sheety.co/b28fcec91afb2fa755e5e2e7484b8495/workoutTracking/workouts', json=data, headers=sheet_header)
    print(rest.text)