import json
import os

from app import logger, create_app
from app.controllers import EventsController
from fast_api.g_calendar import get_calendar_events


def handler(event, context):
    """
    Handles the event and retrieves the next 2 events from the user's Google calendar.

    :param event: The event triggered by the application.
    :type event: dict

    :param context: The context of the event.
    :type context: dict

    :returns: None
    """
    with create_app(os.getenv('FLASK_CONFIG') or 'DEV').app_context():
        logger.info('Processing events')

        events_controller = EventsController()

        # Get the body of the event
        event_body = event["Records"][0]["body"]

        # Parse the body of the event
        event = json.loads(event_body)

        greeting = 'Hey Adrian, I will get your next 2 events from your Google calendar'
        print(greeting)


        thread, run = get_calendar_events()

        wait_on_run(run, thread)
