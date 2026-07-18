from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Any


class APIResponse(BaseModel):

    success: bool
    message: str
    request_id: str
    server_time: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    data: Any | None = None