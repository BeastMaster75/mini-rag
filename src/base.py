from fastapi import FastAPI, APIRouter
from utils.config import get_settings
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome():
    app_setings = get_settings()
    app_name = app_setings.APP_NAME
    app_version = app_setings.APP_VERSION
    return {"name": app_name, "version": app_version}
    