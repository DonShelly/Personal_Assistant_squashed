class Executor:
    """
    Class Executor

    The Executor class is a singleton class that provides methods for executing commands.

    Methods:
    - getInstance(): Returns the singleton instance of the Executor class.
    - execute_write(command): Executes the given command and returns the result.
    - execute_read(command): Executes the given command and returns the result.

    Example usage:
    ```
    executor = Executor.getInstance()
    result = executor.execute_write(command)
    ```
    """
    __instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if not Executor.__instance:
            Executor()
        return Executor.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Executor.__instance:
            raise Exception("This class is a singleton!")
        else:
            Executor.__instance = self

    @staticmethod
    def execute_write(command):
        """
        Executes the given command and returns the result.

        :param command: The command to execute.
        :type command: Command

        :return: The result of executing the command.
        :rtype: Any
        """
        return command.execute()

    @staticmethod
    def execute_read(command):
        return command.execute()
