import re
from typing import Tuple

from core.abc.grabber import Grabber

class DiscordHaxx(Grabber):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def analyse(self) -> Tuple[str, bool]:
        self.regex = re.compile(
            r'(\\Users\\iLinked\\)',
            re.IGNORECASE
        )

        return (
            'DiscordHaxx', self._analyse(self.regex)
        )