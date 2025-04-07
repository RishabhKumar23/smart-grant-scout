from fastapi import FastAPI
from app.models import UserProfile
from app.mcp_context import set_user_profile, get_user_profile

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Smart Grant Scout MCP Agent"}


@app.post("/user-profile")
def update_profile(profile: UserProfile):
    set_user_profile(profile)
    return {"status": "updated"}


@app.get("/user-profile")
def fetch_profile():
    profile = get_user_profile()
    return profile
