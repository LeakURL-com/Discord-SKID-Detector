import re
from typing import List, Tuple

from core.abc import Matcher

class Words(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(token|appdata|leveldb|Local Storage|ipify|discord_webhook|s_localApplicationDataPath|dhooks|grab|steal)',
            re.IGNORECASE
        )
        
        return self._find(
            regex=self.regex,
            type='suspect words'
        )