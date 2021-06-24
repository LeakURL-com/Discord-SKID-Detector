import re
from typing import List, Tuple

from core.abc import Grabber

class Wodx(Grabber):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def analys(self) -> Tuple[str, bool]:
        self.regex = re.compile(
            r'(def find_tokens\(path\)\:[\n\ ]+path \+= \'\\\\Local Storage\\\\leveldb\'[\n\ ]+tokens = \[\])',
            re.IGNORECASE
        )

        return (
            'Wodx\'s grabber', self._analys(self.regex)
        )