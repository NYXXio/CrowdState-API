from datetime import datetime, timezone

from app.core.database import SessionLocal
from app.models.sensor import Sensor
from app.schemas.footfall import FootfallEventCreate
from app.services.footfall_service import FootfallService

db = SessionLocal()

sensor = db.query(Sensor).first()

payload = FootfallEventCreate(
    event_type="ENTRY",
    event_time=datetime.now(timezone.utc),
    occupancy_after_event=5
)

event = FootfallService.ingest_event(
    db=db,
    sensor=sensor,
    payload=payload
)

print(event.id)