import base64
import sys
import re

from core.abc import Matcher, Grabber
from core.logging import Logging
from core.banner import Banner
from core import __version__
from core.file import File

from matchers.regexs import Regexs
from matchers.words import Words
from matchers.webhook import Webhook
from matchers.pastebin import Pastebin
from matchers.code import Code

from grabbers.fgrabber import FGrabber
from grabbers.wodx import Wodx
from grabbers.wodx2 import Wodx2

from rich.box import ROUNDED
from rich.table import Table

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
        __version__,
        len(grabbers),
        len(matchers)
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
r'b64decode\(.*?["\']([a-zA-Z0-9\_=]+)[\"\']',
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

    table = Table(
        header_style='red',
        box=ROUNDED,
        expand=True,
    )

    table.add_column(
        'Line',
        overflow=None,
        style='bright_black'
    )

    table.add_column(
        'Content',
        overflow=None,
        style='cyan'
    )

    table.add_column(
        'Type',
        overflow=None,
        style='cyan'
    )

    results = {}

    for grabber in grabbers:

        grabber_name, result = grabber(
            content=content
        ).analys()

        if result:

            Logging.success(
                f'known token grabber detected: [bold red]"{grabber_name}"[/bold red]'
            )

    for matcher in matchers:

        _results = matcher(
            content=content
        ).find()

        for result in _results:
            line, group, type = result

            try:
                results[line].append((group, type))
            except:
                results[line] = [(group, type)]

    if not results:
        Logging.error(
            'nothing found.'
        )

        sys.exit()

    for k in sorted(results):
        for result in results[k]:
            group, type = result
            table.add_row(
                str(k), group, type
            )

    console.print(
        table,
    )

    Logging.success(
        'done'
    )

if __name__ == '__main__':
    main()