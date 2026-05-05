from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logger import logger
from app.db.init_db import init_db

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

logger.info("App started")

app.include_router(api_router, prefix="/api/v1")

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

@app.get("/")
def root():
    return {"message": "API is running."}