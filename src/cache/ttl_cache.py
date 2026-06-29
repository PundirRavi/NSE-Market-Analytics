import time
from typing import Any

from src.utils.logger import get_logger



class TTLCache:

    def __init__(self, ttl_seconds: int = 30) -> None:

        self.ttl_seconds=ttl_seconds
        
        self._cache: dict[str, dict[str, Any]]={}

        self.logger = get_logger(self.__class__.__name__)

    def get(self, key: str):

        item=self._cache.get(key)

        if item is None:

            self.logger.info(
                "Cache miss for key=%s",
                key
            )

            return None 
        
        age = (
            time.time() - item["timestamp"]
        )

        if age > self.ttl_seconds:

            self.logger.info(
                "Cache expired for key=%s age=%s",
                key,
                round(age, 2)
            )

            
        
            return item["value"]
    
    def set(
            self,
            key: str, 
            value
    ):

        self._cache[key]={
            "value": value,
            "timestamp": time.time()
        }

        self.logger.info(
            "Cache updated for key=%s",
            key
        )

    def clear(self):

        self._cache.clear()
        self.logger.info(
            "Cache cleared"
        )
