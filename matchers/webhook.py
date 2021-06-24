import re
from typing import List, Tuple

from core.abc import Matcher

class Webhook(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'((:?https:\/\/discord.*?)\d{18}?[^[a-z0-9\-_][a-z0-9\-_]{68})',
            re.IGNORECASE
        )

        return self._find(
            regex=self.regex,
            type='discord webhook'
        )