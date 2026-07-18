from sqlalchemy import Column, BigInteger, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Sensor(Base):

    __tablename__ = "sensors"

    id = Column(BigInteger, primary_key=True)

    business_id = Column(
        BigInteger,
        ForeignKey("businesses.id")
    )

    sensor_uid = Column(
        Text,
        unique=True,
        nullable=False
    )

    installed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    active = Column(
        Boolean,
        default=True
    )

    business = relationship(
        "Business",
        back_populates="sensors"
    )

    footfall_events = relationship(
        "FootfallEvent",
        back_populates="sensor"
    )

    hourly_summaries = relationship(
        "HourlySummary",
        back_populates="sensor"
    )

    predictions = relationship(
        "Prediction",
        back_populates="sensor"
    )

    api_key_hash = Column(
        Text,
        unique=True,
        nullable=False
    )