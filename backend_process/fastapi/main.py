from fastapi import FastAPI, HTTPException, APIRouter
from .db import add_user_rec, get_user_data_rec
from .models import NewClient, Partner, Recommendations, GroupRecs
from ..recommendation.main import find_similarity
from typing import List

app = FastAPI(docs_url="/")


@app.post('/client', tags=["Client Functions"], response_model=NewClient)
async def new_partner(client: NewClient):
    try:
        id = add_user_rec(client.id, client.features, client.cuisine, cost=None)
        if id['id'] == "err":
            raise HTTPException(status_code=id['status_code'], detail=id['details'])
        return {
            "id": id['id'],
            "features": client.features,
            "cuisine": client.cuisine,
        }
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.get("/client/{id}/recommendations", tags=["Client Functions"], response_model=Recommendations)
async def get_user_rec(id: str):
    try:
        ans = get_user_data_rec(id)
        if ans['id'] == "err":
            raise HTTPException(status_code=ans['status_code'], detail=ans['details'])
        return {"recs": find_similarity(ans)}
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.get('/client/{id}/info', tags=["Client Functions"])
async def get_user_data(id: str):
    try:
        ans = get_user_data_rec(id)
        if ans['id'] == "err":
            raise HTTPException(status_code=ans['status_code'], detail=ans['details'])
        return ans
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.post("/algorithm", tags=["Group Functions"])
async def algorithm_many(group_info: GroupRecs): #пока тупое решение
    try:
        features = group_info.features
        users_recommendations = group_info.users_recommendations
        cuisine = set()
        for user in users_recommendations:
            for rec in user:
                cuisine.add(rec)
        return {
            'result': find_similarity({
                'features': features,
                'cuisine': list(cuisine)
            }, result_amount=10)
        }
    except Exception as e:
        print(group_info)
        raise HTTPException(500, detail=str(e))
