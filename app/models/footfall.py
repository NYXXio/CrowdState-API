from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class FootfallEvent(Base):

    __tablename__ = "footfall_events"

    id = Column(BigInteger, primary_key=True)

    sensor_id = Column(
        BigInteger,
        ForeignKey("sensors.id")
    )

    event_type = Column(
        Text,
        nullable=False
    )

    event_time = Column(
        DateTime(timezone=True),
        nullable=False
    )

    event_uuid = Column(
        String(36),
        unique=True,
        nullable=False,
        index=True
    )

    occupancy_after_event = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sensor = relationship(
        "Sensor",
        back_populates="footfall_events"
    )