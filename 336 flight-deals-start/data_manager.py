import requests
from pprint import pprint

simple_sheety_api = 'https://api.sheety.co/fd3a246e69abdd6250a53eafa321960d/flightDeals/prices'
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_response = requests.get(url=simple_sheety_api)
        self.data = self.sheety_response.json()
        pprint(self.data)
        # self.prices_list = self.data['prices']

    def get_price(self):
        return self.data['prices']

    def update_destination_codes(self):
        for dataset in self.prices_list:
            self.id = dataset['id']
            sheety_api = f'{simple_sheety_api}/{self.id}'
            sheet_input = {
                'price': {
                    'iataCode': dataset['iataCode']
                }
            }
            iatacode_response = requests.put(url=sheety_api, json=sheet_input)


