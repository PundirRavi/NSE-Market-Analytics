import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from core.logger import logger
from infra.exceptions.api_exceptions import (
    APITimeoutError,
    APIConnectionError
)


class BaseClient:

    def __init__(self):

        self.session = requests.Session()

        retries = Retry(
            total=5,
            connect=5,
            read=5,
            backoff_factor=2,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504
            ]
        )

        adapter = HTTPAdapter(max_retries=retries)

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get(self, url, **kwargs):

        try:

            logger.info(f"Calling API: {url}")

            response = self.session.get(
                url,
                **kwargs
            )

            response.raise_for_status()

            return response

        except requests.exceptions.Timeout as exc:

            logger.error(f"Timeout: {url}")

            raise APITimeoutError(str(exc))

        except requests.exceptions.ConnectionError as exc:

            logger.error(f"Connection Error: {url}")

            raise APIConnectionError(str(exc))