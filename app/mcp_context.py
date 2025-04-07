import json
from pathlib import Path
from typing import Optional, List
from .models import UserProfile, GrantPreferences
from pydantic import BaseModel


class SearchQuery(BaseModel):
    query: str
    timestamp: str


class MCPContext(BaseModel):
    user_profile: Optional[UserProfile] = None
    grant_preferences: Optional[GrantPreferences] = None
    search_history: List[SearchQuery] = []


MOCK_USER_ID = "masa_user_0x123"
CONTEXT_FILE = Path("masa_context.json")


def get_user_id():
    return MOCK_USER_ID


def load_context() -> MCPContext:
    if CONTEXT_FILE.exists():
        try:
            with open(CONTEXT_FILE, "r") as f:
                all_data = json.load(f)
                user_data = all_data.get(get_user_id(), {})
                return MCPContext(**user_data)
        except json.JSONDecodeError:
            pass
    return MCPContext()


def save_context(context: MCPContext):
    all_data = {}
    if CONTEXT_FILE.exists():
        try:
            with open(CONTEXT_FILE, "r") as f:
                all_data = json.load(f)
        except json.JSONDecodeError:
            pass
    all_data[get_user_id()] = context.dict()
    with open(CONTEXT_FILE, "w") as f:
        json.dump(all_data, f, indent=2)


def set_user_profile(profile: UserProfile):
    ctx = load_context()
    ctx.user_profile = profile
    save_context(ctx)


def get_user_profile() -> Optional[UserProfile]:
    return load_context().user_profile


def set_grant_preferences(prefs: GrantPreferences):
    ctx = load_context()
    ctx.grant_preferences = prefs
    save_context(ctx)


def get_grant_preferences() -> Optional[GrantPreferences]:
    return load_context().grant_preferences
