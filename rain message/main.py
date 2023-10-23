import requests
from twilio.rest import Client

auth_token = '640cf88cb5b55ea6d6d1463da3c14843'
account_sid = 'AC90c30b099dbb4b41efa06e099bb3dab8'


parameters = {
    'lat': 31.520370,
    'lon': 74.358749,
    'appid': '7b4018440c66c3aae48ca2ec3a7bb4f0',
    'exclude': 'current,minutely,daily'
}


response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()

data_slice = data['hourly'][:12]

will_rain = False

for hour in data_slice:
    weather_condition = hour['weather'][0]['id']
    if weather_condition < 700:
        will_rain = True

#if will_rain:
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="It is going to rain today. Bring an umbrella",
    from_='+19805505811',
    to='+923224381967'
)
print(message.status)