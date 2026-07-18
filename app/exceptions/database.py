from app.exceptions.base import CrowdStateException


class DatabaseUnavailableError(

    CrowdStateException

):

    def __init__(self):

        super().__init__(

            "Database unavailable.",

            503

        )