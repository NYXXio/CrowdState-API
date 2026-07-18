from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from app.core.database import get_db
from app.schemas.response import APIResponse

from app.exceptions.database import DatabaseUnavailableError

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


def verify_database(db: Session):

    try:
        db.execute(text("SELECT 1"))

    except OperationalError:
        raise DatabaseUnavailableError()


@router.get("/live")
def live(request: Request):

    return APIResponse(
        success=True,
        message="Application is alive.",
        request_id=request.state.request_id
    )


@router.get("/ready")
def ready(
    request: Request,
    db: Session = Depends(get_db)
):

    verify_database(db)

    return APIResponse(
        success=True,
        message="Application is ready.",
        request_id=request.state.request_id
    )