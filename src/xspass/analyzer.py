import re
from typing import Dict, List
from .utils import get_char_sets

class Analyzer:
    def __init__(self):
        self.chars = get_char_sets()
    
    def analyze(self, password: str) -> Dict:
        return {
            'length': len(password),
            'entropy': self._entropy(password),
            'score': self._score(password),
            'crack_time': self._crack_time(password),
            'issues': self._find_issues(password)
        }
    
    def _entropy(self, password: str) -> float:
        charset_size = self.chars.get_size_for_password(password)
        return len(password) * (charset_size.bit_length())
    
    def _score(self, password: str) -> int:
        score = 0
        score += len(password) >= 12
        score += bool(re.search(r'[a-z]', password))
        score += bool(re.search(r'[A-Z]', password))
        score += bool(re.search(r'\d', password))
        score += bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]', password))
        return score

    def _crack_time(self, password: str) -> str:
        combinations = self.chars.get_size_for_password(password) ** len(password)
        seconds = combinations / (100_000_000_000)
        
        if seconds < 60: return f"{seconds:.1f}s"
        if seconds < 3600: return f"{seconds/60:.1f}m"
        if seconds < 86400: return f"{seconds/3600:.1f}h"
        if seconds < 31536000: return f"{seconds/86400:.1f}d"
        return f"{seconds/31536000:.1f}y"

    def _find_issues(self, password: str) -> List[str]:
        issues = []
        if len(password) < 12:
            issues.append("short")
        if re.search(r'123|abc|qwerty', password.lower()):
            issues.append("common_pattern")
        if re.search(r'(.)\1{2,}', password):
            issues.append("repeated_chars")
        return issues 