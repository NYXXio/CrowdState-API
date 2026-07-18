from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models

from app.core.config import settings

from app.api.version import router as version_router

from app.api.ingest import router as ingest_router
from app.api.health import router as health_router

from app.middleware.request_logger import RequestLoggingMiddleware
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text

from app.core.database import engine


from contextlib import asynccontextmanager

from app.core.logging import logger

from app.middleware.request_context import RequestContextMiddleware

from app.exceptions.base import CrowdStateException

from app.exceptions.exception_handler import (
    crowdstate_exception_handler,
    generic_exception_handler
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(

        f"Starting CrowdState API | "

        f"Version=1.0.0 | "

        f"Environment={settings.ENVIRONMENT}"

    )

    yield

    logger.info(

        "Stopping CrowdState API"

    )

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(RequestContextMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(
    CrowdStateException,
    crowdstate_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

app.include_router(ingest_router)

app.include_router(health_router)

app.include_router(version_router)

@app.get("/")
def root():

    return {
        "service":"CrowdState API",
        "status":"running"
    }