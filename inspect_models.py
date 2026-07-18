from app.models.sensor import Sensor
from app.models.footfall import FootfallEvent

print("Sensor attributes:")
print(sorted(k for k in Sensor.__dict__.keys() if not k.startswith("_")))

print("\nFootfallEvent attributes:")
print(sorted(k for k in FootfallEvent.__dict__.keys() if not k.startswith("_")))