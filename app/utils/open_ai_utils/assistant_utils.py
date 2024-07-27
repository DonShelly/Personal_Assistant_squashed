import json
import logging
import os
import time
from pprint import pprint

from dotenv import load_dotenv
from openai import OpenAI

ADHD_ASSISTANT_ID = 'asst_yec2RY4O4bSgAzYLIuL54Fnf'

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def show_json(obj):
    pprint(json.loads(obj.model_dump_json()))


logger = logging.getLogger(__name__)
try:
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
except Exception as e:
    logger.error(f'Error getting OpenAI API key from .env file: {e}')


def create_message(thread, calendar_voice_preface, calendar_output):
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="assistant",
        content=calendar_voice_preface
    )

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=calendar_output
    )


def execute_thread(thread, assistant_id):
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )
    return run


def submit_message(assistant_id, thread, calendar_voice_preface, calendar_output):
    create_message(thread, calendar_voice_preface, calendar_output)
    run = execute_thread(thread, assistant_id)
    return run


def get_response(thread):
    # Fetch all messages in the conversation thread
    messages = client.beta.threads.messages.list(thread_id=thread.id, order="desc").data

    # Iterate over messages in reverse chronological order
    for message in messages:
        print(f'Debug: {message}')

        # If the message is from the AI model, return the content of the message
        if message.role == 'assistant':
            return message.content[0].text.value

            # If no assistant message was found, return some default string or handle the error as you see fit
    return "No assistant message found"


def create_calendar_thread_and_run(calendar_voice_preface, calendar_output):
    thread = client.beta.threads.create()
    run = submit_message(ADHD_ASSISTANT_ID, thread, calendar_voice_preface, calendar_output)
    return thread, run


# Pretty printing helper for debugging
def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()


# Waiting in a loop
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run
