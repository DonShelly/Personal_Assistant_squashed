import os
import pathlib

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from app import logger
from settings import get_app_var


class GoogleAuthorisationFlow:
    """

    GoogleAuthorisationFlow class handles the authorization flow for accessing the Google Calendar API.

    Attributes:
    - GOOGLE_OAUTH2_TOKEN_PATH: The path to the file that stores the user's access and refresh secrets.
    - CLIENT_SECRET_FILE_PATH: The path to the file that contains the client secret credentials.
    - GOOGLE_CALENDAR_API_SCOPE: The scope of the Google Calendar API.

    Methods:
    - validate_calendar_api_creds(): Validates the credentials for accessing the Google Calendar API. If the credentials are not available or not valid, it prompts the user to log in and saves the credentials for the next run.

    """
    def __init__(self):
        self.GOOGLE_OAUTH2_TOKEN_PATH = get_app_var('GOOGLE_OAUTH2_TOKEN_PATH')
        self.CLIENT_SECRET_FILE_PATH = get_app_var('GOOGLE_CLIENT_SECRET_FILE_PATH')
        self.GOOGLE_CALENDAR_API_SCOPE = get_app_var('GOOGLE_CALENDAR_API_SCOPE')

    def validate_calendar_api_creds(self):
        """
        Validates the Google Calendar API credentials.

        This method checks if the credentials file exists and are valid. If the credentials are not valid or do not exist, it attempts to refresh them if possible. If refreshing the credentials fails, it unlinks the credentials file and prompts the user to log in again.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        creds = None
        # The file token.json stores the user's access and refresh secrets, and is
        # created automatically when the authorization flow completes for the first
        # time.

        logger.debug(f'GOOGLE_OAUTH2_TOKEN_PATH')

        if os.path.exists(self.GOOGLE_OAUTH2_TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(self.GOOGLE_OAUTH2_TOKEN_PATH, self.GOOGLE_CALENDAR_API_SCOPE)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                # TODO: Make this actually catch exception (does not do that currently)
                except RefreshError as e:
                    logger.error(
                        f'Command: {self.__class__.__name__} \n'
                        f'{e} \n'
                        f'Attempting to refresh credentials with unlink()...'
                    )
                    try:
                        pathlib.Path(self.GOOGLE_OAUTH2_TOKEN_PATH).unlink()
                        try:
                            creds.refresh(Request())
                        except RefreshError as e:
                            logger.error(
                                f'Command: {self.__class__.__name__} \n'
                                f'{e} \n'
                            )
                    except OSError as e:
                        logger.error(
                            f'Command: {self.__class__.__name__} \n'
                            f'{e.filename} - {e.strerror}'
                        )
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CLIENT_SECRET_FILE_PATH,
                    self.GOOGLE_CALENDAR_API_SCOPE
                )
                creds = flow.run_local_server(port=get_app_var('AUTH_FLOW_LOCAL_SERVER_PORT'))
            # Save the credentials for the next run
            with open(self.GOOGLE_OAUTH2_TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())
