from sqlalchemy.orm import Session

from app.models.sensor import Sensor
from app.models.footfall import FootfallEvent
from app.schemas.footfall import FootfallEventCreate

from app.core.logging import logger


class FootfallService:

    @staticmethod
    def ingest_event(
        db: Session,
        sensor: Sensor,
        payload: FootfallEventCreate
    ) -> int:

        existing = (
            db.query(FootfallEvent)
            .filter(
                FootfallEvent.event_uuid == payload.event_uuid
            )
            .first()
        )

        if existing:

            logger.info(
                f"Duplicate event ignored: "
                f"{payload.event_uuid}"
            )

            return existing.id

        try:

            event = FootfallEvent(
                sensor_id=sensor.id,
                event_uuid=payload.event_uuid,
                event_type=payload.event_type.value,
                event_time=payload.event_time,
                occupancy_after_event=payload.occupancy_after_event
            )

            db.add(event)

            db.flush()

            event_id = event.id

            db.commit()

            logger.info(
                f"Stored event {event_id} "
                f"for sensor {sensor.sensor_uid}"
            )

            return event_id

        except Exception:

            db.rollback()

            logger.exception(
                "Database commit failed."
            )

            raise