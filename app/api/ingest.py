from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import time

from app.core.database import get_db
from app.core.logging import logger

from app.schemas.footfall import FootfallEventCreate
from app.schemas.response import APIResponse

from app.services.footfall_service import FootfallService

from app.security.auth import authenticate_sensor

from app.models.sensor import Sensor

from fastapi import Request

from app.exceptions.sensor import (
    SensorNotFoundError,
    SensorInactiveError
)

router = APIRouter(
    prefix="/ingest",
    tags=["Sensor Ingestion"]
)

@router.post("/")
def ingest_event(
    request: Request,
    payload: FootfallEventCreate,
    sensor: Sensor = Depends(authenticate_sensor),
    db: Session = Depends(get_db)
):

    event_id = FootfallService.ingest_event(
        db=db,
        sensor=sensor,
        payload=payload
    )

    return APIResponse(

        success=True,

        message="Footfall event stored successfully.",

        request_id=request.state.request_id,

        data={

            "event_id": event_id

        }

    )