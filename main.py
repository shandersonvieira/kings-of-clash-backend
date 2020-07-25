from fastapi import FastAPI
from routers import war_api
from settings import Settings
from functools import lru_cache

Settings()

app = FastAPI()

app.include_router(war_api.router)
