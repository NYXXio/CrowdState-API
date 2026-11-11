
from pydantic import BaseModel, Field


class HeartbeatCreate(BaseModel):

    uptime_seconds: int = Field(ge=0)

    wifi_rssi: int = Field(ge=-127, le=0)

    firmware_version: str = Field(
        min_length=1,
        max_length=50
    )
