from flask import Blueprint, send_file

from app.controllers.events_controller import EventsController
from app.controllers.speach_controller import SpeachController
from app.decorators import handle_exceptions

calendar_events_routes = Blueprint("calendar_event_routes", __name__)
calendar_events_controller = EventsController()
elvenlabs_speach_controller = SpeachController()


@calendar_events_routes.route("/", methods=["GET"])
@handle_exceptions
def get_all_events():
    """
    GET all events.

    Returns the human-readable speech file of all events in the calendar.

    Returns:
        The human-readable speech file (audio file) of all events in the calendar.
    """
    events = calendar_events_controller.get_all_events()
    human_readable_text = calendar_events_controller.get_human_readable_text(events)
    speach_file = elvenlabs_speach_controller.get_speach_file(human_readable_text)
    return send_file(speach_file)
