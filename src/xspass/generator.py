from .utils import get_char_sets
from secrets import choice, token_bytes
from typing import List

class Generator:
    def __init__(self):
        self.chars = get_char_sets()
    
    def generate(self, length: int = 12, upper: bool = True,
                digits: bool = True, special: bool = True,
                similar: bool = False) -> str:
        chars = self.chars.get_charset(upper, digits, special, similar)
        return ''.join(choice(chars) for _ in range(length))

    def recovery_code(self) -> str:
        chars = self.chars.alphanumeric
        return '-'.join(''.join(choice(chars) for _ in range(4)) for _ in range(3))