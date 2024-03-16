from qkiqsh import request_for_id, request_rest_data
from olimp import create_table, insert_data, backup_postgresql
import os

""" основное действие с датасетом происходит здесь. ваша задача
переформатировать данные из экселя в data_places в формате json(пример place_data)
"""


def start():
    create_table()
    key = os.environ.get('API_KEY')
    data_places = []
    place_data = {
        "name" : "",
        "lat" : "",
        "long" : "",
        "id" : ""
    }

    for place in data_places:
        place_data['name'] = place[0]
        place_data['lat'] = place[1]
        place_data['long'] = place[2]
        location_id = request_for_id(key, place_data['name'], place_data['lat'], place_data['long'])
        json_data = request_rest_data(location_id, key)
        insert_data(json_data)

    backup_postgresql()
