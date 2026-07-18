from app.exceptions.base import CrowdStateException


class SensorNotFoundError(CrowdStateException):

    def __init__(self, sensor_uid):

        super().__init__(
            message=f"Sensor '{sensor_uid}' not found.",
            status_code=404
        )


class SensorInactiveError(CrowdStateException):

    def __init__(self, sensor_uid):

        super().__init__(
            message=f"Sensor '{sensor_uid}' is disabled.",
            status_code=403
        )