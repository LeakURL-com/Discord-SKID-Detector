import re

from abc import ABC, abstractmethod

from typing import Dict, List, Tuple

class Matcher(ABC):
    
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def find(self) -> None:
        pass

    def get_lines(self) -> List[Tuple[int, str]]:
        lines = []

        for line in self.content.splitlines():
            lines.append(
                (len(lines) + 1, line.strip())
            )

        return lines

    def _find(self, regex: re.Pattern) -> List[Tuple[int, str, re.Match]]:
        lines = self.get_lines()
        found = []

        for line, line_content in lines:
            match = regex.search(
                line_content
            )

            if match:
                found.append(
                    (line, line_content, match)
                )
        
        return found