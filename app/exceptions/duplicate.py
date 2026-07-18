from app.exceptions.base import CrowdStateException

class DuplicateEventError(

    CrowdStateException

):

    def __init__(self, event_uuid):

        super().__init__(

            message=f"Duplicate event '{event_uuid}'.",

            status_code=409

        )