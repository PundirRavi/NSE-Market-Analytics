from requests import Session
from requests.exceptions import RequestException

from src.exceptions.custom_exceptions import ClientException
from src.utils.logger import get_logger


class BaseClient:
    def __init__(
        self,
        base_url: str,
        timeout: int,
        headers: dict[str, str],
    ) -> None:
        self.base_url = base_url
        self.timeout = timeout

        self.session = Session()
        self.session.headers.update(headers)

        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str) -> dict:
        url = f"{self.base_url}{endpoint}"

        try:
            self.logger.info(
                "Sending GET request to %s",
                url
            )

            response = self.session.get(
                url,
                timeout=self.timeout,
            )

            response.raise_for_status()

            self.logger.info(
                "Request successful: %s",
                url
            )

            return response.json()

        except RequestException as exc:
            self.logger.exception(
                "Request failed: %s",
                url
            )

            raise ClientException(
                f"Failed to call endpoint: {url}"
            ) from exc