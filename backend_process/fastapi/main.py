from fastapi import FastAPI, HTTPException, APIRouter
from .db import add_user, get_user_data
from .models import NewClient

app = FastAPI(docs_url="/")


@app.post('/client', tags=["Endpoints"], response_model=NewClient)
async def new_partner(client: NewClient):
    try:
        id = add_puser(client.client_id, client.features, client.cuisine, cost=None)
        print(0)
        return {
            "id": id['id'],
            "client_id": client.client_id,
            "features": client.features,
            "cuisine": client.cuisine,
        }
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@app.get('/client/{id}/suggest', tags=["Endpoints"], response_model=NewClient)
async def get_user_data(id: str):
    try:
        return get_user_data(id)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

