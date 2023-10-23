import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'eisha'
TOKEN = 'tngvoevmf12efrgthy'
ID = 'graph1'

today = datetime.now()
DATE = today.strftime('%Y%m%d')
QUANTITY = '7'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text )

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': ID,
    'name': 'Book Reading Graph',
    'unit': 'page',
    'type': 'int',
    'color': 'momiji',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

add_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{ID}'

pixels_params = {
    'date': DATE,
    'quantity': QUANTITY,
}

pixel_header = {
    'X-USER-TOKEN': TOKEN
}
# add_pixel_response = requests.post(url=add_pixel_endpoint, json=pixels_params, headers=pixel_header)
# print(add_pixel_response.text)

update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}'

update_params = {
    'quantity': '1'
}
# update_response = requests.put(url=update_pixel_endpoint, json=update_params, headers=pixel_header)
# print(update_response.text)

delete_response_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}'
delete_response = requests.delete(url=delete_response_endpoint, headers=pixel_header)
print(delete_response.text)
