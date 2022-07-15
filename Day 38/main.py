"""
Workout Tracker project
"""
import requests as req
from datetime import  datetime

APP_ID="4104dd5d"
API_KEY="9e55885f1aeeb7a330e97a03cfd3fb89"
NLP_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"


GENDER = "Male"
WEIGHT_KG = "83"
HEIGHT_CM = "171"
AGE = "26"


headers = {
    "x-app-id":APP_ID,
    "x-app-key": API_KEY,
    'Content-Type':'application/json'

}

user_input = input("Tell me which exercise you did?:")

data= {
    "query":user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}
response =  req.post(url=NLP_ENDPOINT, json= data, headers=headers)
result = response.json()

# print(result)


#getting todays date
today = datetime(year = 2022, month = 7, day=13 )
today = today.strftime("%d/%m/%Y/")

#Getting time 
time = datetime.now()
current_time = time.strftime("%X")



#post request input for sheet: Date, time, Exercise, Duration, Calories
duration=[]
calories=[]
exercise = []

for i, j in result.items():
    #print(j)
    for x in j:
        duration.append(x["duration_min"])
        calories.append(x['nf_calories'])
        exercise.append(x['name'])

#Making post request into sheety
SHEETY_URL= "https://api.sheety.co/ee104b0ed113f19e4089a547163bd7e4/myWorkouts/workouts"

for i in range(len(duration)):
    POST_data = {
        "workout":{
            "Date":today,
            "Time":current_time,
            "Exercise": exercise[i],
            "Duration": duration[i],
            "Calories": calories[i]
        }
    }

    # print(POST_data)

    response = req.post(url=SHEETY_URL, json=POST_data)
    print(response.text)



