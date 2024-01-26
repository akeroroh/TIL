import requests
from pprint import pprint as print

API_BASE_URL = 'https://jsonplaceholder.typicode.com/users/'
dummy_data = []

for i in range(1, 11):
    API_URL = f'{API_BASE_URL}{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    if -80 < lat < 80 and -80 < lng < 80:
        dummy_dict = {
            'company' : parsed_data['company']['name'],
            'lat' : lat,
            'lng' : lng,
            'name' : parsed_data['name']
        }
        dummy_data.append(dummy_dict)

print(dummy_data)