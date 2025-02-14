import string
from dataclasses import dataclass

@dataclass
class CharacterSets:
    lower: str = string.ascii_lowercase
    upper: str = string.ascii_uppercase
    digits: str = string.digits
    special: str = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    similar: str = "iI1loO0"
    alphanumeric: str = string.ascii_uppercase + string.digits

    def get_charset(self, upper: bool, digits: bool, special: bool, avoid_similar: bool) -> str:
        chars = self.lower
        if avoid_similar:
            chars = ''.join(c for c in chars if c not in self.similar)
        if upper:
            chars += self.upper
        if digits:
            chars += self.digits
        if special:
            chars += self.special
        return chars

    def get_size_for_password(self, password: str) -> int:
        size = 0
        if any(c in self.lower for c in password): size += 26
        if any(c in self.upper for c in password): size += 26
        if any(c in self.digits for c in password): size += 10
        if any(c in self.special for c in password): size += 32
        return size

def get_char_sets() -> CharacterSets:
    return CharacterSets() 