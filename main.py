import argparse
import base64
import re

from core.dataclasses import Data
from core.logging import Logging
from core.banner import Banner
from core.file import File

from modules.matchers.code import Code
from modules.matchers.words import Words
from modules.matchers.regexs import Regexs
from modules.matchers.webhook import Webhook
from modules.matchers.pastebin import Pastebin

from modules.grabbers.discordhaxx import DiscordHaxx
from modules.grabbers.wodx import Wodx
from modules.grabbers.wodx2 import Wodx2
from modules.grabbers.fgrabber import FGrabber

Data.register(Code)
Data.register(Words)
Data.register(Regexs)
Data.register(Webhook)
Data.register(Pastebin)

Data.register(DiscordHaxx)
Data.register(FGrabber)
Data.register(Wodx)
Data.register(Wodx2)


def main() -> None:
    console = Logging.console

    parser = argparse.ArgumentParser(
    )

    parser.add_argument(
        '-f', '--file',
        required=True,
        type=str,
        help='File to look up.',
        metavar='',
        dest='file'
    )

    Banner.print(
    )

    args = parser.parse_args()

    file = args.file

    ext = File.get_file_ext(file)

    Logging.info(
        f'starting...'
    )

    content = File.read_file_content(
        file
    )

    # bypass base64 encode obfuscation method for python.
    if ext == 'py':
        found = 0
        tmp_content = content

        while 1:
            exprs = re.findall(
r'b64decode\(.*?[\"\']([a-zA-Z0-9\_=]+)[\"\']',
            )

            if not exprs:

                if bool(found):
                    content += tmp_content

                break

            found = 1

            Logging.success(
                f'found base64 encoded expression!'
            )

            tmp_content = ''

            for expr in exprs:
                tmp_content += base64.b64decode(
                    expr.encode()
                ).decode()

    for grabber in Data.get_grabbers():

        grabber_name, result = grabber(
            content=content
        ).analyse()

        if result:
            Logging.success(
                f'known token grabber detected: [bold red]"{grabber_name}"[/bold red]'
            )

    for matcher in Data.get_matchers():

        results, type = matcher(
            content=content
        ).find()

        results = list(results)
        
        console.print(
            f'\n[red]@[/red] [white underline]{type}[/white underline]'
        )

        if not results:
            console.print(
                f'[red]╰[/red] nothing found'
            )

            continue


        for code in results[:-1]:
            console.print(
                f'[red]├[/red] {code[0] if isinstance(code, tuple) else code}'
            )

        code = results[len(results) - 1]

        console.print(
            f'[red]╰[/red] {[0] if isinstance(code, tuple) else code}'
        )

    Logging.success(
        'done'
    )

if __name__ == '__main__':
    main()
