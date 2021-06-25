import re
from typing import List, Tuple

from core.abc import Matcher

class Regexs(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(r?[\"\']?mfa.*?\\\..*?(:?\{84\}[\"\']?|\+)|r?[\"\']?.*?\{24\}.*?\{6\}.*?\{27\}[\"\']?)',
        )
        
        return self._find(
            regex=self.regex,
            type='malicious regex'
        )