from src.clients.base_client import BaseClient

from src.models.option_chain import (
    OptionChainResponse
)

from src.models.config.config_models import NSEConfig

from src.utils.logger import get_logger 


class OptionChainClient(BaseClient):
    def __init__(
            self, 
            config: NSEConfig,
            session
    ) -> None:
        
        super().__init__(
                session=session,
                base_url= config.base_url,
                timeout=config.timeout
        )

        self.logger=get_logger(
            self.__class__.__name__
            )

        self.endpoint=(
            config.datasets.option_chain.endpoint

        )

    def get_option_chain(
            self, 
            symbol: str,
            expiry: str
        ) -> OptionChainResponse:
        
        self.logger.info(
            "Fetching option chain for %s",
            symbol
        )

        response=self.get(
            endpoint=self.endpoint,
            params={
            "type": "Indices",
            "symbol": symbol,
            "expiry": expiry,
    },
        )

        return OptionChainResponse.model_validate(
            response
        )