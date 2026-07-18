from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class EventType(str, Enum):
    ENTRY = "ENTRY"
    EXIT = "EXIT"


class FootfallEventCreate(BaseModel):

    event_type: EventType

    event_time: datetime

    event_uuid: str

    occupancy_after_event: int = Field(
        ge=0
    )