from ingestion.clients.base_client import BaseClient

from ingestion.models.market_status import MarketStatusResponse

class NSEClient(BaseClient):

    BASE_URL = "https://www.nseindia.com"

    def __init__(self):
        super().__init__()

        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0.0.0 Safari/537.36"
                ),
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://www.nseindia.com/",
                "Connection": "keep-alive",
            }
        )

        # Bootstrap cookies
        self.session.get(
            self.BASE_URL,
            timeout=20
        )

    def get_market_status(self) -> MarketStatusResponse:

        response = self.get(
            f"{self.BASE_URL}/api/marketStatus",
            timeout=20
        )

        payload = response.json()

        return MarketStatusResponse.model_validate(
            payload
        )