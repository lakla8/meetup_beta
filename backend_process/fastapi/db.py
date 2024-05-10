from pymongo import MongoClient
from bson import json_util, ObjectId
from typing import List, Dict, Any

mongodb_host = 'mongodb://localhost'
mongodb_port = 27017
db_name = 'meetup'
collection_name = 'users'


def set_up(mongodb_host, mongodb_port, db_name, collection_name):
    client = MongoClient(host=mongodb_host,port=mongodb_port)

    dbs = client[db_name]
    collections = dbs[collection_name]
    return dbs, collections


db, collection = set_up(mongodb_host, mongodb_port, db_name, collection_name)


def add_user(id: str, features : list, cuisine : list, cost : None) -> dict[str, str]:
    return {
        "id" : str(
            collection.insert_one(
                {
                    "features": features,
                    "cuisine": cuisine,
                    "cost": None,
                }
            ).inserted_id
        ),
        "client_id": id,
    }


def get_user_data(id: str) -> dict:
    res = collection.find_one({'_id': ObjectId(id)})
    return {
        "id": str(res['_id']),
        "features": res["festures"],
        "cuisine": res["cuisine"],
        "cost": res["cost"]
    }



