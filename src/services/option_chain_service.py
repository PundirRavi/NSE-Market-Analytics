from src.utils.logger import get_logger
from src.models.option_chain import OptionChainResponse

class OptionChainService:

    def __init__(
        self,
        client,
        cache
    ):
        self.client = client
        self.cache = cache

        self.logger = get_logger(
            self.__class__.__name__
        )

    def fetch_option_chain(
        self,
        symbol: str
    ) -> OptionChainResponse:
        
        #removing expiry logic as of now from here
        #expiry = self.expiry_service.get_current_expiry(symbol)

        cache_key = (
            f"option_chain:{symbol}"
        )

        cached = self.cache.get(
            cache_key
        )

        if cached:

            self.logger.info(
                "Returning cached option chain for %s",
                symbol
            )

            return OptionChainResponse.model_validate(cached)

        self.logger.info(
            "Fetching option chain from NSE for %s",
            symbol
        )

        response = (
            self.client.get_option_chain(
                symbol
            )
        )

        parsed = OptionChainResponse.model_validate(response)

        self.cache.set(
            cache_key,
            parsed.model_dump()
        )

        return parsed