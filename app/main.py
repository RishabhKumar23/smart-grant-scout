from fastapi import FastAPI, Query
from typing import List, Optional
from .models import UserProfile, GrantPreferences, Grant
from .mcp_context import (
    set_user_profile,
    get_user_profile,
    set_grant_preferences,
    get_grant_preferences,
)
import json
from pathlib import Path

app = FastAPI(title="Smart Grant Scout Agent (MASA Subnet 59)")

# Load mock grants
GRANTS_FILE = Path("data/grants.json")
if not GRANTS_FILE.exists():
    GRANTS_FILE.parent.mkdir(exist_ok=True)
    sample_grants = [
        {
            "id": "grant_001",
            "title": "Youth STEM Education Grant",
            "description": "Funding for organizations improving STEM access.",
            "funding_amount": 15000,
            "sector": ["education", "youth"],
            "deadline": "2025-05-30",
            "source_url": "https://example.com/grants/001",
        },
        {
            "id": "grant_002",
            "title": "Clean Energy Community Grant",
            "description": "Support for nonprofits promoting renewable energy education.",
            "funding_amount": 20000,
            "sector": ["renewable energy", "education"],
            "deadline": "2025-06-15",
            "source_url": "https://example.com/grants/002",
        },
    ]
    with open(GRANTS_FILE, "w") as f:
        json.dump(sample_grants, f, indent=2)


def load_grants() -> List[Grant]:
    with open(GRANTS_FILE, "r") as f:
        data = json.load(f)
        return [Grant(**item) for item in data]


@app.get("/")
def root():
    return {"message": "Smart Grant Scout Agent is live (MASA Subnet 59)"}


@app.post("/user-profile")
def update_profile(profile: UserProfile):
    set_user_profile(profile)
    return {"status": "User profile updated"}


@app.get("/user-profile")
def fetch_profile():
    profile = get_user_profile()
    return profile or {"message": "No profile set"}


@app.post("/grant-preferences")
def update_preferences(prefs: GrantPreferences):
    set_grant_preferences(prefs)
    return {"status": "Preferences updated"}


@app.get("/grant-preferences")
def fetch_preferences():
    prefs = get_grant_preferences()
    return prefs or {"message": "No preferences set"}


@app.get("/search-grants", response_model=List[Grant])
def search_grants(keyword: Optional[str] = Query(None), min_amount: int = 0):
    grants = load_grants()
    results = []
    for g in grants:
        if (
            keyword
            and keyword.lower() not in g.title.lower()
            and keyword.lower() not in g.description.lower()
        ):
            continue
        if g.funding_amount and g.funding_amount < min_amount:
            continue
        results.append(g)
    return results
