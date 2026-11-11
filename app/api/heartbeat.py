
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.security.auth import authenticate_sensor

from app.models.sensor import Sensor
from app.schemas.heartbeat import HeartbeatCreate
from app.schemas.response import APIResponse


router = APIRouter(
    prefix="/heartbeat",
    tags=["Sensor Heartbeat"]
)


@router.post("/")
def receive_heartbeat(
    request: Request,
    payload: HeartbeatCreate,
    sensor: Sensor = Depends(authenticate_sensor),
    db: Session = Depends(get_db)
):

    sensor.last_seen_at = datetime.now(timezone.utc)

    sensor.uptime_seconds = payload.uptime_seconds

    sensor.wifi_rssi = payload.wifi_rssi

    sensor.firmware_version = payload.firmware_version

    db.commit()

    return APIResponse(
        success=True,
        message="Sensor heartbeat received successfully.",
        request_id=request.state.request_id,
        data={
            "sensor_uid": sensor.sensor_uid,
            "last_seen_at": sensor.last_seen_at,
            "status": "ONLINE"
        }
    )
