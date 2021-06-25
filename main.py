import base64
import sys
import re

from core.abc import Matcher, Grabber
from core.logging import Logging
from core.banner import Banner
from core import __version__
from core.file import File

from matchers.code import Code
from matchers.words import Words
from matchers.regexs import Regexs
from matchers.webhook import Webhook
from matchers.pastebin import Pastebin

from grabbers.wodx import Wodx
from grabbers.wodx2 import Wodx2
from grabbers.fgrabber import FGrabber

matchers = [x for x in (
    Regexs,
    Words,
    Webhook,
    Pastebin,
    Code
) if issubclass(x, Matcher)]

grabbers = [x for x in (
    FGrabber,
    Wodx,
    Wodx2
) if issubclass(x, Grabber)]

def main() -> None:
    console = Logging.console

    Banner.print(
    )

    if len(sys.argv) != 2:
        Logging.error(
            f'python3.9 {sys.argv[0]} <file>'
        )

        sys.exit()

    file = sys.argv[1]

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
                tmp_content
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

    for grabber in grabbers:

        grabber_name, result = grabber(
            content=content
        ).analys()

        if result:
            Logging.success(
                f'known token grabber detected: [bold red]"{grabber_name}"[/bold red]'
            )

    for matcher in matchers:

        results, type = matcher(
            content=content
        ).find()
        
        console.print(
            f'\n[red]@[/red] [white underline]{type}[/white underline]'
        )

        if not bool(results):
            console.print(
                f'[red]|_[/red] nothing found'
            )

        for code in results:
            console.print(
                f'[red]|_[/red] {code[0] if isinstance(code, tuple) else code}'
            )

    Logging.success(
        'done'
    )

if __name__ == '__main__':
    main()