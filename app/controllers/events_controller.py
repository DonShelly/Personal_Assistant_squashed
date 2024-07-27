from app.commands.events import (
    GetAllEventsCommand,
    GetHumanReadableTextCommand,
)
from app.controllers.controller import Controller


class EventsController(Controller):
    """

    This class represents an EventsController that inherits from Controller.

    Methods:
    - get_all_events(): Executes the read operation using the GetAllEventsCommand and returns the result.
    - get_human_readable_text(events): Executes the read operation using the GetHumanReadableTextCommand with the provided events and returns the result.

    """
    def get_all_events(self):
        return self.executor.execute_read(GetAllEventsCommand())

    def get_human_readable_text(self, events):
        return self.executor.execute_read(GetHumanReadableTextCommand(events))
