import requests

KIWI_API = "https://tequila-api.kiwi.com"
KIWI_API_KEY = 'zKQUpqmJVPRlawwQFzbwepuJRTcvSSZB'
class FlightSearch():
    #This class is responsible for talking to the Flight Search API.

    def destination_code(self, city):
        header = {
            'apikey': KIWI_API_KEY
        }
        params = {
            'term': city,
            'location_types': 'city',
        }
        location_endpoint = f'{KIWI_API}/locations/query'
        response = requests.get(url=location_endpoint, headers=header, params=params)
        data = response.json()
        code = data['locations'][0]['code']
        return code



