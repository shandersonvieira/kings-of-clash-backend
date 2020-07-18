from fastapi import FastAPI
from routers import war
from settings import Settings
from functools import lru_cache

@lru_cache()
def get_settings():
    return Settings()

get_settings()

app = FastAPI()

app.include_router(war.router)
