from app.commands.get_speach import GetSpeachFileCommand
from app.controllers.controller import Controller


class SpeachController(Controller):
    """
    The `SpeachController` class is a subclass of `Controller` and provides a method to get the speech file associated with a given human readable text.

    Attributes:
        None

    Methods:
        get_speach_file: Executes the `GetSpeachFileCommand` with the provided human readable text and returns the speech file.

    """
    def get_speach_file(self, human_readable_text):
        return self.executor.execute_read(GetSpeachFileCommand(human_readable_text))
