import re
from typing import List, Tuple

from core.abc import Matcher
from core.logging import Logging



class Regexs(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(m.*?f.*?a.*?\\\..*?(:?\{84\}|\+)|.*?\{24\}.*?\{6\}.*?\{27\})',
            re.IGNORECASE
        )

        found = []

        for line, line_content, match in self._find(self.regex):
            n = 0
            while 1:
                try:
                    group = match.group(n)

                    if group:
                        found.append((line, group, 'malicious regex'))

                    n += 1
                except:
                    break

        return set(found)