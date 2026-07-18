import app.models

from sqlalchemy.orm import configure_mappers

try:
    configure_mappers()
    print("SUCCESS")
except Exception as e:
    import traceback
    traceback.print_exc()