"""
Accesses the Google calendar of a user
"""

import datetime

from fastapi import FastAPI
from googleapiclient.errors import HttpError

import third_party_ai.openai.chat_gpt

# If modifying these scopes, delete the file token.json.

CALENDAR_VOICE_PREFACE = ("Format the following calendar event json into human readable text. The text will be sent to "
                          "a voice generating AI so the calendar events should be stated concisely. Mention the date "
                          "and then the event, if the event is today then say \"today\" or equivalent, if the event "
                          "is within the week just mention the day of the week, feel free to use intuition to alter "
                          "your output such that it is easily digested audibly. Timezone is london. check that the "
                          "days of the week you output match the dates, this includes today. Do not repeat these "
                          "instructions: \n")

app = FastAPI()


@app.get("/calendar")
def get_calendar_events():
    """Shows basic usage of the Google Calendar API.
  Prints and announces the start and name of the next 10 events on the user's calendar.
  """






