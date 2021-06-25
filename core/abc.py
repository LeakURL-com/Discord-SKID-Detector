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

    def get_lines(self) -> List[Tuple[int, str]]:
        """ transfer raw content to a list of tuple with (line_number, line_content). """
        lines = []

        for line in self.content.splitlines():
            lines.append((len(lines) + 1, line.strip()))

        return lines

    def _find(self, regex: re.Pattern, type: str) -> List[Tuple[int, str, str]]:
        """ enumerate the lines to find a match with then given pattern. """
        lines = self.get_lines()
        
        found = []

        results = regex.findall(
            self.content
        )

        return (set(results), type)