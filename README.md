# Discord Malware Detector 🚙
### _make discord skidz angry_


UPDATED 12/2022 BY YOUR GUYS AT LEAKURL.COM!!!!! SEE US @@ LEAK.TOOLS ALSO MY GUYS AND LEAKS.SHOP! HAVING A GANDER!


DMD is a program that reads the content of a given file and looks for common things that are found in token stealers.

![](./imgs/1.png)

## Features

- decodes base64 strings
- looks for malicious regexps
- looks for suspicious words
- looks for webhooks URL
- looks for pastebin.com links

## Create your own grabber

Grabbers are stored in /grabbers/.
To create your own, just create a file (ex: my_grabber.py).
Then just copy this template:
```python
import re
from typing import List, Tuple

from core.abc import Grabber

class My_Grabber(Grabber):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def analyse(self) -> Tuple[str, bool]:
        self.regex = re.compile(
            r'()', # your regular expression here, do not forget the ( ) 
            re.IGNORECASE
        )

        return (
            'Grabber name', 
            self._analyse(self.regex) # self._alalys() is a bool value, so you can use other ways (checksums, 'string' if self.content etc.)
        )
```

for sure in `main.py` you need to import your matcher with `from grabbers.my_grabber import MyGrabber` then add it to the matchers list:
```
grabbers = (
    ...,
    MyGrabber
)
```

## Create your own matcher

Matchers are stored in /matchers/.
To create your own, just create a file (ex: my_matcher.py).
Then just copy this template:
```python
import re
from typing import List, Tuple

from core.abc import Matcher

class MyMatcher(Matcher):
    def __init__(self, content: str) -> None:
        super().__init__(content)

    def find(self) -> List[Tuple[int, str, str]]:
        self.regex = re.compile(
            r'()', # your regular expression here, do not forget the ( ) 
            re.IGNORECASE
        )
        
        return self._find(
            regex=self.regex,
            type='' # result type (ex: discord webhook?, suspect word? etc, can be whatever you want)
        )
```

for sure in `main.py` you need to import your matcher with `from modules.my_module import MyMatcher` then add it to the matchers list:
```
matchers = (
    ...,
    MyMatcher
)
```

 ## s/o to...
 - [Vichy](https://github.com/Its-Vichy) for the idea
 - [sql](https://github.com/sql69) for the new webhook regex.
