"""Adds a voice to the AI text generated"""

import requests
from pydub import AudioSegment
from pydub.playback import play
import re

from settings import get_app_var


def speak_text(text):
    """
    Speaks the given text using the 'Alice' voice from ElevenLabs.

    Args:
        text (str): The text to be spoken.

    Returns:
        None
    """
    chunk_size = 2000
    # Alice's voice
    url = "https://api.elevenlabs.io/v1/text-to-speech/RqyG7oymUXW0NnNRxlLa"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": get_app_var('XI_API_KEY')
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_192",
        "voice_settings": {
            "stability": 1,
            "similarity_boost": 1
        }
    }
    print("Getting ElvenLabs 'Alice' voice audio...")

    response = requests.post(url, json=data, headers=headers)

    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
            else:
                print("Voice resolve error")
                
    speach = AudioSegment.from_file('output.mp3', format="mp3")
    play(speach)


def vet_emoji(json):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', json)
