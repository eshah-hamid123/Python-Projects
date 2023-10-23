
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

dataman = DataManager()
sheet_data = dataman.get_price()
print(sheet_data)
iatacode = []
for data in sheet_data:
    if data['iataCode'] == '':
        flightsearch = FlightSearch()
        data['iataCode'] = flightsearch.destination_code(data['city'])
        iatacode.append(data['iataCode'])
        flight_data = FlightData()
        flight_data.flight(data['iataCode'])


for code in iatacode:
    flight_data = FlightData()
    flight_data.flight(code)

# dataman.update_destination_codes()

