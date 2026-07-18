from time import perf_counter
from sqlalchemy import text

from app.core.database import SessionLocal

db = SessionLocal()

for i in range(5):

    start = perf_counter()

    db.execute(text("SELECT 1"))

    print(f"{i+1}: {(perf_counter()-start)*1000:.2f} ms")