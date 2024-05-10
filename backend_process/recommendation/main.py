""" основное действие с датасетом происходит здесь. ваша задача
переформатировать данные из экселя в data_places в формате json(пример place_data)
"""



from qkiqsh import request_for_id, request_rest_data
from olimp import create_json_file
import os, json, numpy as np
from dotenv import load_dotenv


def create_database():
    load_dotenv()
    with open('../../resources/db.json') as f:
        data_places = json.load(f)
    key = os.environ.get('API_KEY')
    json_data = []
    for place_data in data_places:
        location_id = request_for_id(key, place_data['name'], place_data['lot'], place_data['long'])
        if location_id != Exception:
            json_data_place = request_rest_data(location_id, key)
            json_data.append(json_data_place)

    create_json_file(json_data, "../resources/database.json")


def get_features_unique(data_places):
    temporary_set = set()
    for data in data_places:
        try:
            for feature in data['features']:
                temporary_set.add(feature)
        except KeyError as err:
            continue
    return temporary_set


def get_cuisine_unique(data_places):
    temporary_set = set()
    for data in data_places:
        try:
            for food in data["cuisine"]:
                temporary_set.add(food['name'])
        except KeyError as err:
            continue
    return temporary_set


def cosine_similarity(array1, array2):
    return np.dot(array1, array2) / (np.linalg.norm(array1) * np.linalg.norm(array2))


def list_coherence(array1, array2, c=0.0):
    return [c if x not in array1 else 1.0 for x in array2]


def make_change():
    with open('../../resources/database.json') as f:
        data_places = json.load(f)['data_list']

    abs_f = get_features_unique(data_places)
    abs_c = get_cuisine_unique(data_places)

    print(abs_f)
    print(abs_c)

    for place in data_places:
        try:
            place['features_abs'] = list_coherence(place['features'], abs_f)
        except Exception as err:
            place['features_abs'] = [0.0] * len(abs_f)

        try:
            temporary_data = [types['name'] for types in place['cuisine']]
            place['cuisine_abs'] = list_coherence(temporary_data, abs_c)
        except Exception as err:
            place['cuisine_abs'] = [0.0] * len(abs_c)

    create_json_file(data_places, '../resources/database.json')


def clear_errors():
    with open('../../resources/database.json') as f:
        data_places = json.load(f)['data_list']

    for place in data_places[:]:
        if 'error' in list(place.keys()):
            print(place)
            data_places.remove(place)

    create_json_file(data_places, '../resources/database.json')


def find_similarity(client, db_filename: str = '../resources/database.json'):
    with open(db_filename) as f:
        data_places = json.load(f)['data_list']

    abs_f = get_features_unique(data_places)
    abs_c = get_cuisine_unique(data_places)

    print(abs_f)
    print(abs_c)

    features = list_coherence(client['features'], abs_f, c=0.65)
    cuisine = list_coherence(client['cuisine'], abs_c, c=-1.0)

    best_results = []

    for place in data_places:
        print(place)
        f_angle = cosine_similarity(features, place["features_abs"])
        c_angle = cosine_similarity(cuisine, place['cuisine_abs'])
        if str(f_angle) == "nan" or str(c_angle) == "nan":
            pass
        else:
            best_results.append([place['name'], place['features'], place['cuisine'], cosine_similarity([f_angle, c_angle], [1.0, 1.0])])

    best_results.sort(key=lambda x: x[3], reverse=True)

    return best_results[:5]





