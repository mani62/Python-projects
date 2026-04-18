from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

logger.info("App started")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API is running."}