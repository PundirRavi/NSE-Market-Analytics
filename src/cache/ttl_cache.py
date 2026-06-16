import time
from typing import Any

class TTLCache:

    def __init__(self, ttl_seconds: int = 30) -> None:
        self.ttl_seconds=ttl_seconds

        self._value: Any = None 
        self._last_updated: float = 0 

    def get(self):

        if self._value is None:
            return None 
        
        age = time.time() - self._last_updated

        if age > self.ttl_seconds:
            return None 
        
        return self._value
    
    def set(self, value):

        self._value = value 
        self._last_updated = time.time()

    def clear(self):

        self._value=None
        self._last_updated=0
