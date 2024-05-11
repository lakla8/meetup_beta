from pydantic import BaseModel
from typing import List


class NewClient(BaseModel):
    id: str
    features: List[str]
    cuisine: List[str]


class GroupRecs(BaseModel):
    features: List[str]
    users_recommendations: List[List[str]]


class Partner(BaseModel):
    id: str
    features: List[str]
    cuisine: List[str]


class Recommendations(BaseModel):
    recs: List[List]


class GroupResults(BaseModel):
    result: dict