from rich.console import Console

class Logging:
    console = Console()

    @staticmethod
    def print(prefix: str, prefix_color: str, message: str) -> None:
        """ prints a message with a prefix. """
        Logging.console.print(
            f'[{prefix_color}][{prefix}][/{prefix_color}] [white]{message}[/white]'
        )

    @staticmethod
    def success(message: str) -> None:
        """ prints a success message. """
        Logging.print(
            f'+', 'green bold', message
        )

    @staticmethod
    def error(message: str) -> None:
        """ prints an error message. """
        Logging.print(
            f'-', 'red bold', message
        )

    @staticmethod
    def info(message: str) -> None:
        """ prints an info message. """
        Logging.print(
            f'*', 'cyan bold', message
        )

    @staticmethod
    def found(line: int, group: str, type: str) -> None:
        """ prints a "found" message. """
        Logging.console.print(
            f''' 
found {type} at line {line}
-> "{group}"
            '''
        )