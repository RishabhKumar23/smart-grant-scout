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


class SearchQuery(BaseModel):
    query: str
    timestamp: str


class MCPContext(BaseModel):
    user_profile: Optional[UserProfile] = None
    grant_preferences: Optional[GrantPreferences] = None
    search_history: List[SearchQuery] = []
