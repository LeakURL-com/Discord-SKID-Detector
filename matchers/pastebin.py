import re
from typing import List, Tuple

from core.abc import Matcher

class Pastebin(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(https:\/\/pastebin\.com\/(:?raw\/)[a-z0-9]{8})',
        )

        return self._find(
            regex=self.regex,
            type='pastebin link'
        )