import requests
from datetime import datetime, timedelta
SEARCH_API = 'https://tequila-api.kiwi.com/v2/search'
KIWI_API_KEY = 'zKQUpqmJVPRlawwQFzbwepuJRTcvSSZB'
date = datetime.now()
date_now = date.strftime('%d/%m/%Y')

return_date = datetime.now() + timedelta(days=180)
return_date = return_date.strftime('%d/%m/%Y')

class FlightData:
    #This class is responsible for structuring the flight data.
    def flight(self, code):
        header = {
            'apikey': KIWI_API_KEY
        }
        params = {
            'fly_from': 'LHE',
            'fly_to': code,
            'dateFrom': date_now,
            'dateTo': return_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=SEARCH_API, params=params, headers=header)
        data = response.json()
        print(data)


