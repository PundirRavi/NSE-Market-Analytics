from requests import Session
from requests.exceptions import RequestException

from src.exceptions.custom_exceptions import ClientException
from src.utils.logger import get_logger


class BaseClient:
    def __init__(
        self,
        session: Session,
        base_url: str,
        timeout: int
    ) -> None:
        self.session = session
        self.base_url = base_url
        self.timeout = timeout

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

            self.logger.info(
                "Status Code: %s",
                response.status_code
            )

            print(response.text[:500])
            

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