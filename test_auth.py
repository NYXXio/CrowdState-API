from app.core.database import SessionLocal
from app.models.sensor import Sensor
from app.security.hashing import hash_api_key

db = SessionLocal()

api_key = "cs_live_570ca23fb25446cb79c0bc772088e72670ac1164231d30c20f733c36de1f24fc"

sensor = (
    db.query(Sensor)
    .filter(Sensor.api_key_hash == hash_api_key(api_key))
    .first()
)

print(sensor)

if sensor:
    print(sensor.sensor_uid)
    print(sensor.active)
else:
    print("Sensor not found")