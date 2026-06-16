from src.clients.base_client import BaseClient
from src.models.config_models import NSEConfig
from src.models.market_status import MarketStatusResponse


class MarketStatusClient(BaseClient):
    def __init__(self, config: NSEConfig) -> None:
        super().__init__(
            base_url=config.base_url,
            timeout=config.timeout,
            headers=config.headers,
        )

        self.endpoint = config.datasets["market_status"].endpoint

    def get_market_status(self) -> MarketStatusResponse:
        response = self.get(self.endpoint)

        return MarketStatusResponse.model_validate(response)