from pydantic import BaseModel
from typing import List

class NewClient(BaseModel):
    id: str
    client_id: str
    features: List[str]
    cuisine: List[str]


class Partner(BaseModel):
    id: str
    features: List[str]
    cuisine: List[str]