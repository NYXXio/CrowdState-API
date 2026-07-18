from fastapi import Header
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.config import settings

from app.models.sensor import Sensor

from app.security.hashing import hash_api_key

from app.core.logging import logger

import time

def authenticate_sensor(
    x_api_key: str = Header(alias=settings.API_KEY_HEADER),
    db: Session = Depends(get_db)
):

    api_key_hash = hash_api_key(
        x_api_key
    )

    start = time.perf_counter()
    api_key_hash = hash_api_key(x_api_key)

    sensor = (
        db.query(Sensor)
        .filter(
            Sensor.api_key_hash == api_key_hash
        )
        .first()
    )

    if sensor is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    if not sensor.active:
        raise HTTPException(
            status_code=403,
            detail="Sensor disabled"
        )

    return sensor