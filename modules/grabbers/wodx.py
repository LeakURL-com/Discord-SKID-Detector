import re
from typing import Tuple

from core.abc.grabber import Grabber

class Wodx(Grabber):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def analyse(self) -> Tuple[str, bool]:
        self.regex = re.compile(
            r'(def find_tokens\(path\)\:[\n\ ]+path \+= \'\\\\Local Storage\\\\leveldb\'[\n\ ]+tokens = \[\])',
            re.IGNORECASE
        )

        return (
            'Wodx\'s grabber', self._analyse(self.regex)
        )
