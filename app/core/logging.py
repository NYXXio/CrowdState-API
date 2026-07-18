import logging
import sys

from app.core.config import settings


logger = logging.getLogger("crowdstate")

logger.setLevel(settings.LOG_LEVEL)

# Prevent duplicate logs if imported multiple times
logger.handlers.clear()

console_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    "%Y-%m-%d %H:%M:%S"
)

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Don't propagate to the root logger
logger.propagate = False