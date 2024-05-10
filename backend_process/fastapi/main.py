from fastapi import FastAPI, HTTPException, APIRouter
from db import add_user, get_user_data
from models import NewClient, Partner, Recommendations
from ..recommendation.main import find_similarity

app = FastAPI(docs_url="/")


@app.post('/client', tags=["Endpoints"], response_model=NewClient)
async def new_partner(client: NewClient):
    try:
        id = add_user(client.client_id, client.features, client.cuisine, cost=None)
        return {
            "id": id['id'],
            "client_id": client.client_id,
            "features": client.features,
            "cuisine": client.cuisine,
        }
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.get("/client/{id}/recommendations", tags=["Endpoints"], response_model=Recommendations)
async def get_user_rec(client_id: str):
    try:
        return {client_id: find_similarity(get_user_data(client_id))}
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.get('/client/{id}/info', tags=["Endpoints"], response_model=Partner)
async def get_user_data(client_id: str):
    try:
        return get_user_data(client_id)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

