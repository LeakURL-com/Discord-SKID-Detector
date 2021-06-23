from rich.console import Console

class Logging:
    console = Console()

    @staticmethod
    def print(prefix: str, prefix_color: str, message: str) -> None:
        Logging.console.print(
            f'[{prefix_color}][{prefix}][/{prefix_color}] [white]{message}[/white]'
        )

    @staticmethod
    def info(message: str) -> None:
        Logging.print(
            f'*', 'cyan bold', message
        )

    @staticmethod
    def found(line: int, group: str, type: str) -> None:
        Logging.console.print(
            f''' 
found {type} at line {line}
-> "{group}"
            '''
        )