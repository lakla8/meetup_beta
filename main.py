from qkiqsh import request_for_id, request_rest_data
from olimp import create_json_file
import os, json
from dotenv import load_dotenv


""" основное действие с датасетом происходит здесь. ваша задача
переформатировать данные из экселя в data_places в формате json(пример place_data)
"""


def start():
    load_dotenv()
    with open('db.json') as f:
        data_places = json.load(f)
    key = os.environ.get('API_KEY')
    json_data = []
    for place_data in data_places:
        location_id = request_for_id(key, place_data['name'], place_data['lot'], place_data['long'])
        if location_id != Exception:
            json_data_place = request_rest_data(location_id, key)
            json_data.append(json_data_place)

    create_json_file(json_data, "database.json")

start()


