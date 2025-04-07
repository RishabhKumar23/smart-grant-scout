import json
from pathlib import Path
from app.models import MCPContext, UserProfile, GrantPreferences, SearchQuery
from datetime import datetime

# Simulate MASA MCP store with a local JSON file
CONTEXT_FILE = Path("masa_context.json")


def load_context() -> MCPContext:
    if CONTEXT_FILE.exists():
        with open(CONTEXT_FILE, "r") as f:
            data = json.load(f)
        return MCPContext(**data)
    return MCPContext()


def save_context(context: MCPContext):
    with open(CONTEXT_FILE, "w") as f:
        json.dump(context.dict(), f, indent=2)


# Example: update user profile
def set_user_profile(profile: UserProfile):
    ctx = load_context()
    ctx.user_profile = profile
    save_context(ctx)


# Example: retrieve user profile
def get_user_profile() -> UserProfile:
    return load_context().user_profile
