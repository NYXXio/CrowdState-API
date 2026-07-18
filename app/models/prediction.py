from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.core.database import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(BigInteger, primary_key=True)

    sensor_id = Column(
        BigInteger,
        ForeignKey("sensors.id")
    )

    prediction_for = Column(
        DateTime(timezone=True),
        nullable=False
    )

    predicted_entries = Column(Numeric)

    predicted_exits = Column(Numeric)

    predicted_average_occupancy = Column(Numeric)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sensor = relationship(
    "Sensor",
    back_populates="predictions"
    )