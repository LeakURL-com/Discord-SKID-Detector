import re

from abc import (
    ABC, 
    abstractmethod
)

from typing import Tuple

class Grabber(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def analyse(self) -> Tuple[str, bool]:
        pass

    def _analyse(self, regex: re.Pattern) -> bool:        
        return bool(
            regex.search(self.content)
        )