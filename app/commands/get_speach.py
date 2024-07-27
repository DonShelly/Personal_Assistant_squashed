import os

import openai

from app import logger
from app.core.commands import ReadCommand




def validate() -> bool:
    """
    Returns a boolean value indicating whether the validation is successful.

    :return: True if the validation is successful, otherwise False.
    :rtype: bool
    """
    return True


class GetSpeachFileCommand(ReadCommand):
    """
    Executes the command and generates a speech file.

    :return: The path of the speech file generated.
    :rtype: str

    Example usage:
        obj = MyClass()
        speech_file_path = obj.execute()
    """
    def __init__(self, human_readable_text):
        self.human_readable_text = human_readable_text

    def execute(self):
        """
        Executes the command and generates a speech file.

        Parameters:
            None

        Returns:
            str: The path of the speech file generated.

        Example usage:
            obj = MyClass()
            speech_file_path = obj.execute()
        """
        logger.debug(
            f'Command: {self.__class__.__name__} \n'
        )

        response = openai.audio.speech.create(
            model='tts-1',
            voice='alloy',
            input=self.human_readable_text
        )
        response.stream_to_file(SPEACH_FILE_PATH)

        return SPEACH_FILE_PATH
