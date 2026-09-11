from fastapi import FastAPI, APIRouter, Depends
from utils.config import get_settings, Settings
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome(app_setings: Settings = Depends(get_settings)):

    app_name = app_setings.APP_NAME
    app_version = app_setings.APP_VERSION

    return {
        "name": app_name,
        "version": app_version
        }
    