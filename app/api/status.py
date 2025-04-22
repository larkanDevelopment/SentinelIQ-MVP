from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/status")
async def get_status():
    return {
        "status": "ok",
        "version": settings.project_version
    }
