import re
from typing import List, Tuple

from core.abc import Grabber

class Wodx2(Grabber):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def analys(self) -> Tuple[str, bool]:
        self.regex = re.compile(
            r'(325414537030329320151394843687.*?325414537030329320151394843687.*?325414537030329320151394843687.*?)',
        )

        return (
            'Wodx\'s 2nd grabber', self._analys(self.regex)
        )