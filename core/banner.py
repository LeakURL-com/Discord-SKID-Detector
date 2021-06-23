from core.logging import Logging
from core import __version__

class Banner:
    BANNER = r'''[magenta]
        ╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ╔╦╗╔═╗╦  ╦ ╦╔═╗╦═╗╔═╗
         [white]║║║╚═╗║  ║ ║╠╦╝ ║║  ║║║╠═╣║  ║║║╠═╣╠╦╝║╣  [/white]
        ═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╩╩ ╩╩═╝╚╩╝╩ ╩╩╚═╚═╝
                ╔╦╗╔═╗╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗        
                [white] ║║║╣  ║ ║╣ ║   ║ ║ ║╠╦╝[/white] [cyan]by twitter.com/toastakerman[/cyan]
                ═╩╝╚═╝ ╩ ╚═╝╚═╝ ╩ ╚═╝╩╚═ [bright_black]version %s[/bright_black]
    [/magenta]
    '''

    @staticmethod
    def print() -> None:
        """ print the banner to the terminal """
        Logging.console.print(
            Banner.BANNER % __version__
        )