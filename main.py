import base64
import sys
import re

from core.logging import Logging
from core.banner import Banner
from core.file import File

from matchers.regexs import Regexs
from matchers.words import Words
from matchers.webhook import Webhook
from matchers.pastebin import Pastebin

from rich.box import ROUNDED
from rich.table import Table

exts = (
    'py', 'exe', 'js', 'jar'
)

matchers = (
    Regexs,
    Words,
    Webhook,
    Pastebin
)

def main() -> None:
    console = Logging.console

    Banner.print()

    if len(sys.argv) != 2:
        Logging.info(
            f'python3.9 {sys.argv[0]} <file>'
        )

        sys.exit()

    file = sys.argv[1]

    ext = File.get_file_ext(
        file=file
    )

    if not ext in exts:
        Logging.info(
            f'unknown file extension: {ext}'
        )

        sys.exit()

    Logging.info(
        f'target set to file: "{file}"'
    )

    content = File.read_file_content(
        file
    )

    lines = {}

    for line in content.splitlines():
        lines[len(lines) + 1] = line

    Logging.info(
        f'file content lenght: {len(content)} ({len(lines)} lines)'
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

            Logging.info(
                f'found base64 encoded expression!'
            )

            tmp_content = ''

            for expr in exprs:
                tmp_content += base64.b64decode(
                    expr.encode()
                ).decode()



    table = Table(
        header_style='red',
        box=ROUNDED
    )

    table.add_column(
        'Line',
        overflow=None
    )

    table.add_column(
        'Group',
        overflow=None
    )

    table.add_column(
        'Type',
        overflow=None
    )

    _results = {}

    for matcher in matchers:

        results = matcher(
            content=content
        ).find()

        for result in results:
            line, group, type = result

            try:
                _results[line].append((group, type))
            except:
                _results[line] = [(group, type)]

    for k in sorted(_results):
        for result in _results[k]:
            group, type = result
            table.add_row(
                str(k), group, type
            )

    console.print(
        table
    )

    Logging.info(
        'done'
    )

if __name__ == '__main__':
    main()