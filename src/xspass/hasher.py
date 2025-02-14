import hashlib
import base64
from typing import Dict
from secrets import token_bytes

class Hasher:
    def hash(self, password: str, salt: str = None) -> Dict:
        if not salt:
            salt = base64.b64encode(token_bytes(16)).decode()
        
        hasher = hashlib.sha256()
        hasher.update((password + salt).encode())
        hash = base64.b64encode(hasher.digest()).decode()
        
        return {'hash': hash, 'salt': salt}

    def verify(self, password: str, hash_data: Dict) -> bool:
        verify = self.hash(password, hash_data['salt'])
        return verify['hash'] == hash_data['hash'] 