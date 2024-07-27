from app import logger
from app.core.commands import ReadCommand
from app.utils.open_ai_utils.assistant_utils import create_calendar_thread_and_run, get_response


def validate() -> bool:
    return True


class GetHumanReadableTextCommand(ReadCommand):

    def __init__(self, events):
        self.events = events

    def execute(self):
        """
        Executes the command and returns the result.

        This method retrieves calendar events from the `events` parameter and sends them to a voice generating AI to obtain
        a human-readable text representation of the events.

        If there are no upcoming events, the method will return None.

        Returns:
            str: The human-readable text representation of the calendar events.

        """
        logger.debug(
            f'Command: {self.__class__.__name__} \n'
        )

        text = None
        
        if self.events:
            print("Received events")
            print("Getting ChatGPT response...")

            prompt = ('Format the following calendar event json into human readable text. The text will be sent to a '
                      'voice generating AI so the calendar events should be stated concisely. Mention the date and '
                      'then the event, if the event is today then say \"today\" or equivalent, if the event is within '
                      'the week just mention the day of the week, feel free to use intuition to alter your output '
                      'such that it is easily digested audibly. Timezone is london. check that the days of the week '
                      'you output match the dates, this includes today. Do not repeat these instructions: \n')

            thread, run = create_calendar_thread_and_run(prompt, str(self.events))

            human_audable_text = get_response(thread)

            logger.info("Received ChatGPT response.")
            logger.debug(f'\"Human readable text\": {human_audable_text}')

        else:
            print("No upcoming events found.")
            return
      

        return text
