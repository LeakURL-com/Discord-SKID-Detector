import re
from typing import List, Tuple

from core.abc import Matcher

class Words(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(webhook|token|\/api\/webhooks|appdata|leveldb|Local Storage|PING_ME|[\"\']content[\"\'][\]]?[\ +]?[\:\=])',
            re.IGNORECASE
        )
        
        return self._find(
            regex=self.regex,
            type='suspect words'
        )