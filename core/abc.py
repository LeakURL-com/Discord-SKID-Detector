import re

from abc import ABC, abstractmethod

from typing import List, Tuple

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
            lines.append(
                (len(lines) + 1, line.strip())
            )

        return lines

    def _find(self, regex: re.Pattern, type: str) -> List[Tuple[int, str, str]]:
        """ enumerate the lines to find a match with then given pattern. """
        lines = self.get_lines()
        
        found = []

        for line, line_content in lines:
            for obj in regex.findall(
                line_content
            ):
                if isinstance(obj, tuple):
                    obj = obj[0]

                found.append(
                    (line, obj, type)
                )

        return set(found)