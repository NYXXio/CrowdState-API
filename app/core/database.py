from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from app.core.config import settings

from sqlalchemy.engine import make_url

print("DATABASE_URL TYPE:", type(settings.DATABASE_URL).__name__)
print("DATABASE_URL LENGTH:", len(settings.DATABASE_URL))
print("DATABASE_URL START:", repr(settings.DATABASE_URL[:20]))

try:
    parsed = make_url(settings.DATABASE_URL)
    print("DATABASE_URL PARSED:", parsed.drivername, parsed.host, parsed.port)
except Exception as exc:
    print("DATABASE_URL PARSE ERROR:", repr(exc))



engine = create_engine(
    settings.DATABASE_URL,

    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800,
    pool_timeout=30,
    pool_reset_on_return="rollback"
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()