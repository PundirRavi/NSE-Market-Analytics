from src.utils.logger import get_logger


class OptionChainService:

    def __init__(
        self,
        client,
        cache,
        expiry_service,
    ):
        self.client = client
        self.cache = cache
        self.expiry_service=expiry_service

        self.logger = get_logger(
            self.__class__.__name__
        )

    def fetch_option_chain(
        self,
        symbol: str
    ):
        
        expiry = self.expiry_service.get_current_expiry(symbol)

        cache_key = (
            f"option_chain:{symbol}:{expiry}"
        )

        cached = self.cache.get(
            cache_key
        )

        if cached:

            self.logger.info(
                "Returning cached option chain for %s",
                symbol
            )

            return cached

        self.logger.info(
            "Fetching option chain from NSE for %s",
            symbol
        )

        response = (
            self.client.get_option_chain(
                symbol
            )
        )

        self.cache.set(
            cache_key,
            response
        )

        return response