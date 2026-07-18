from datetime import datetime, timezone

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.base import CrowdStateException

from app.core.logging import logger

from fastapi import status

async def crowdstate_exception_handler(
    request: Request,
    exc: CrowdStateException
):

    logger.warning(
        f"Request={request.state.request_id} | "
        f"{exc.message}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "request_id": request.state.request_id,
            "server_time": datetime.now(
                timezone.utc
            ).isoformat(),
            "data": None
        }
    )


from fastapi import status

async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
    f"Request={request.state.request_id} | "
    f"{request.method} {request.url.path} | "
    f"{type(exc).__name__}: {exc}"
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "Internal server error.",
            "request_id": request.state.request_id,
            "server_time": datetime.now(
                timezone.utc
            ).isoformat(),
            "data": None
        }
    )