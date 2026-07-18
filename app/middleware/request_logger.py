import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        start = time.time()

        response = await call_next(request)

        duration = (time.time() - start) * 1000

        request_id = request.state.request_id

        client = request.client.host if request.client else "Unknown"

        logger.info(

            f"Request={request_id} | "

            f"Client={client} | "

            f"{request.method} "

            f"{request.url.path} | "

            f"Status={response.status_code} | "

            f"Time={duration:.2f} ms"

        )

        return response