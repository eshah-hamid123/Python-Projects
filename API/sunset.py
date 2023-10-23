import requests
from datetime import date time

parameters = {
    'lat': 31.520370,
    'lng': 74.358749,
    'formatted': 0,
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data['results']['sunrise']
print(sunrise.split('T')[1].split(':'))

sunset = data['results']['sunset']
print(sunset)