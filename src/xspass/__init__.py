from .generator import Generator
from .analyzer import Analyzer
from .hasher import Hasher

__version__ = "0.3"

generator = Generator()
analyzer = Analyzer()
hasher = Hasher()

def generate(length=12, **kwargs):
    return generator.generate(length=length, **kwargs)

def analyze(password):
    return analyzer.analyze(password)

def hash_password(password, salt=None):
    return hasher.hash(password, salt)

def verify_password(password, hash_data):
    return hasher.verify(password, hash_data) 