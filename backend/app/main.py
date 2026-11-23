from fastapi import FastAPI

from app.core.config import settings
from app.api.health import router as health_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for Smart Afghan Farmer",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Health"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Afghan Farmer API",
        "docs": "/docs",
        "health": "/api/v1/health"
    }