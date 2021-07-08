import re

from abc import (
    ABC, 
    abstractmethod
)

from typing import (
    List, 
    Tuple
)

class Grabber(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def analys(self) -> Tuple[str, bool]:
        pass

    def _analys(self, regex: re.Pattern) -> bool:        
        return bool(
            regex.search(self.content)
        )

class Matcher(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def find(self) -> None:
        pass

    def _find(self, regex: re.Pattern, type: str) -> List[Tuple[int, str, str]]:
        results = regex.findall(
            self.content,
            re.IGNORECASE
        )

        return (set(results), type)