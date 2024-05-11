from pymongo import MongoClient
from bson import json_util, ObjectId
from typing import List, Dict, Any

mongodb_host = 'mongodb://localhost'
mongodb_port = 27017
db_name = 'meetup'
collection_name = 'users'
users_db = {}
serial_id = 0


def set_up(mongodb_host, mongodb_port, db_name, collection_name):
    client = MongoClient(host=mongodb_host,port=mongodb_port)

    dbs = client[db_name]
    collections = dbs[collection_name]
    return dbs, collections


db, collection = set_up(mongodb_host, mongodb_port, db_name, collection_name)


def add_user(id: str, features: list, cuisine: list, cost: int = None) -> dict[str, str]:
    return {
        "id" : str(
            collection.insert_one(
                {
                    "features": features,
                    "cuisine": cuisine,
                    "cost": cost,
                }
            ).inserted_id
        ),
        "client_id": id,
    }


def add_user_rec(id: str, features: list, cuisine: list, cost: int = None) -> dict:
    try:
        if id in users_db:
            return {
                "id": "err",
                "status_code": 400,
                "details": "User is already created"
            }
        users_db[id] = {
            "features": features,
            "cuisine": cuisine,
            "cost": cost,
        }
        return {
            "results": {
                        "features": features,
                        "cuisine": cuisine,
                        "cost": cost,
                    },
            "id": id
        }
    except KeyError:
        return {
            "id": "err",
            "status_code": 404,
            "details": "User is not found"
        }


def get_user_data(id: str) -> dict:
    res = collection.find_one({'_id': ObjectId(id)})
    return {
        "id": str(res['_id']),
        "features": res["features"],
        "cuisine": res["cuisine"],
        "cost": res["cost"]
    }


def get_user_data_rec(id: str) -> dict:
    try:
        res = users_db[id]
        return {
            "id": id,
            "features": res["features"],
            "cuisine": res["cuisine"],
            "cost": res["cost"]
        }
    except KeyError:
        return {
            "id": "err",
            "status_code": 404,
            "details": "User is not found"
        }

