from pydantic import BaseModel
from typing import List, Optional


class UserProfile(BaseModel):
    org_name: str
    location: str
    sector: str


class GrantPreferences(BaseModel):
    min_amount: Optional[int]
    max_amount: Optional[int]
    interests: List[str]


class Grant(BaseModel):
    id: str
    title: str
    description: str
    funding_amount: Optional[int]
    sector: List[str]
    deadline: Optional[str]
    source_url: Optional[str]
