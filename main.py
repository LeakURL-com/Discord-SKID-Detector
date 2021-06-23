import sys
import re

from typing import List

from rich.console import Console

from core.logging import Logging
from core.banner import Banner
from core.file import File

from core.matchers.regexs import Regexs
from core.matchers.words import Words
from core.matchers.webhook import Webhook
from core.matchers.pastebin import Pastebin

from rich.box import ROUNDED
from rich.table import Table

exts = (
    'py', 'exe', 'js', 'jar'
)

matchers = [
    Regexs,
    Words,
    Webhook,
    Pastebin
]

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
                _results[int(line)].append((group, type))
            except:
                _results[int(line)] = [(group, type)]

    for k in sorted(_results):
        results = _results[k]
        for result in results:
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