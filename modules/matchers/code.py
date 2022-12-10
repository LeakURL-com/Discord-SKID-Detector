import re
from typing import List, Tuple

from core.abc.matcher import Matcher

class Code(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'(webhook(:?_url)[\ +]?=?|ping_me[\ +]?=?|\{?[\n +]?[\"\']content[\"\'][\ +]?\:?)',
        )
        
        return self._find(
            regex=self.regex,
            type='suspect code'
        )
    
    
