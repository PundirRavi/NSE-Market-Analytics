
from src.utils.logger import get_logger

class MarketStatusService:

    def __init__(self, client, cache) -> None:
        self.client = client
        self.cache = cache
        self.logger = get_logger(self.__class__.__name__)

    def fetch_market_status(self):
        self.logger.info("Fetching market status data")

        cached = self.cache.get("market_status")

        if cached is not None:

            self.logger.info(
                "Returning market status from cache"
            )

            return cached

        self.logger.info(
            "Fetching market status from NSE"
        )

        response = self.client.get_market_status()

        self.logger.info(
                    "Retrieved %s market states",
                    len(response.marketState)
                )
        
        self.cache.set(
            "market_status",
            response
        )

        return response