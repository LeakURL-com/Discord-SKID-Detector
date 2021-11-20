import re
from typing import List, Tuple

from core.abc.matcher import Matcher

class Webhook(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(https?):\/\/((?:ptb\.|canary\.)?discord(?:app)?\.com)\/api(?:\/)?(v\d{1,2})?\/webhooks\/(\d{17,19})\/([\w\-]{68})',
        )

        return self._find(
            regex=self.regex,
            type='discord webhook'
        )
