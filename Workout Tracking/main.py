import requests
from datetime import datetime

api_key = '03d77ffb540d7fd8f3adcdec6bde65f5'
api_id = '9ec2213c'

ex_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'


headers = {
    'x-app-id' : api_id,
    'x-app-key' : api_key
}


exercise_types = input('What type of exercise did you do? ')
gender = 'female'
age = 20
weight = 54
height = 162.56

params = {
    'query': exercise_types,
    'gender': gender,
    'age': age,
    'weight_kg': weight,
    'height_cm': height
}

ex_response = requests.post(url=ex_endpoint, json=params, headers=headers)
data = ex_response.json()
print(data)

############################## DATETIME #####################################

today = datetime.now()
date = today.strftime('%x')
time = today.strftime('%X')
workout_endpoint = 'https://api.sheety.co/fd3a246e69abdd6250a53eafa321960d/myWorkouts/workouts'


for ex in data['exercises']:
    sheet_input = {
        "workout" : {
            'date': date,
            'time': time,
            'exercise': ex['user_input'].title(),
            'duration': ex['duration_min'],
            'calories': ex['nf_calories']
        }
    }

    workout_response = requests.post (url=workout_endpoint, json=sheet_input, auth=('eisha','sheetyproject'))
    print(workout_response.text)