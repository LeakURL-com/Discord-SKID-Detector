from core.logging import Logging
from core import __version__

class Banner:
    BANNER = r'''[magenta]
[red]@[/red] [white bold]Discord Malware Detector[/white bold] 🚙
[red]|_[/red] [cyan]by twitter.com/toastakerman[/cyan]
[red]|_[/red] [bright_black]version %s[/bright_black]

[white][underline]note:[/underline] this program have been coded to detect malwares that 
      have been copied-pasted from Github by 13yo discord 
      kids feeling haxors, not for 200iq obfuscated grabbers.
[/white]
    '''

    @staticmethod
    def print() -> None:
        """ print the banner to the terminal """
        Logging.console.print(
            Banner.BANNER % __version__
        )