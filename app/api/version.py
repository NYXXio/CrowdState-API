from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(
    prefix="/version",
    tags=["Version"]
)

@router.get("/")
def version():

    return {

        "version":"1.0.0",

        "environment":settings.ENVIRONMENT

    }