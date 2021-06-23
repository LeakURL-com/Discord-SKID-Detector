import re
from typing import List, Tuple

from core.abc import Matcher
from core.logging import Logging

class Words(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(webhook|token|\/api\/webhooks|appdata|leveldb)',
            re.IGNORECASE
        )
        
        found = []

        for line, line_content, match in self._find(self.regex):
            n = 0
            while 1:
                try:
                    group = match.group(n)

                    if group:
                        found.append((line, group, 'webhook'))

                    n += 1
                except:
                    break

        return set(found)