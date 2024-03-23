import requests
"""штука которая спрашивает датасет с триадвайзера"""

def request_for_id(key, name, lat, long):
    url_id = f"https://api.content.tripadvisor.com/api/v1/location/search?key={key}&searchQuery={name}&latLong={lat}%2C%20{long}&language=en"
    headers = {"accept": "application/json"}

    response = requests.get(url_id, headers=headers)
    try:
        json_data = response.json()['data']
        print(json_data)
        location_id = json_data[0]['location_id']
        print(json_data[0]['distance'], json_data[0]['name'])
        return location_id

    except Exception as err:
        print(response.json()['error']['code'])
        print(response.json()['error']['message'])
        print(response.json()['error']['type'])
        return err


def request_rest_data(location_id, key):
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details?key={key}&language=en&currency=RUB"

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    return response.json()








