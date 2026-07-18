from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.core.database import Base


class HourlySummary(Base):

    __tablename__ = "hourly_summary"

    id = Column(BigInteger, primary_key=True)

    sensor_id = Column(
        BigInteger,
        ForeignKey("sensors.id")
    )

    hour_start = Column(
        DateTime(timezone=True),
        nullable=False
    )

    entries = Column(Integer)

    exits = Column(Integer)

    average_occupancy = Column(Numeric)

    maximum_occupancy = Column(Integer)

    minimum_occupancy = Column(Integer)

    closing_occupancy = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sensor = relationship(
    "Sensor",
    back_populates="hourly_summaries"
    )