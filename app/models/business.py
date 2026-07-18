from sqlalchemy import Column, BigInteger, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Business(Base):

    __tablename__ = "businesses"

    id = Column(BigInteger, primary_key=True, index=True)

    business_name = Column(Text, nullable=False)

    address = Column(Text)

    city = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sensors = relationship(
        "Sensor",
        back_populates="business",
        cascade="all, delete-orphan"
    )