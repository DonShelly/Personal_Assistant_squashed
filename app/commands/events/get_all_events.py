import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from app import logger
from app.core.commands import WriteCommand
from app.utils.google_utils.authentication import GoogleAuthorisationFlow


def validate() -> bool:
    return True


class GetAllEventsCommand(WriteCommand):
    """
    The `GetAllEventsCommand` class inherits from the `WriteCommand` class and implements the `execute` method. This class is responsible for executing the command and retrieving calendar events.

    Constructor:
    - `__init__(self)`: Initializes the command by creating an instance of the `GoogleAuthorisationFlow` class and assigning it to the `google_auth_flow` attribute.

    Methods:
    - `execute(self, google_auth_flow=None) -> dict`: Executes the command and retrieves calendar events.

      Parameters:
        - `google_auth_flow (Optional)`: An instance of the `GoogleAuthFlow` class used for authentication. If not provided, the method will use the default `GoogleAuthFlow` instance.

      Returns:
        - `dict`: A dictionary containing the retrieved calendar events.

      Example usage:
        ```python
        google_auth_flow = GoogleAuthFlow()
        result = execute(google_auth_flow)
        ```
    """
    def __init__(self):
        self.google_auth_flow = GoogleAuthorisationFlow()

    def execute(self, google_auth_flow=None) -> dict:
        """

        This method executes a command to retrieve calendar events from the Google Calendar API. It requires the Google authentication flow as an optional parameter.

        Parameters:
        - google_auth_flow: An optional authentication flow object. Defaults to None.

        Returns:
        - A dictionary containing the retrieved calendar events.

        Example Usage:
        ```
        calendar_events = execute(google_auth_flow)
        ```

        """
        logger.debug(
            f'Command: {self.__class__.__name__} \n'
        )

        events = None

        calendar_api_creds = self.google_auth_flow.validate_calendar_api_creds()

        try:
            service = build("calendar", "v3", credentials=calendar_api_creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
            print("Getting calendar events...")
            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    maxResults=2,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])
        except HttpError as error:
            print(f"An error occurred: {error}")

        return events
