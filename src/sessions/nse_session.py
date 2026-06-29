from requests import Session

from src.utils.logger import get_logger


class NSESession:

    def __init__(
        self,
        base_url: str,
        headers: dict[str, str],
        timeout: int
    ) -> None:

        self.base_url = base_url
        self.timeout = timeout

        self.session = Session()
        self.session.headers.update(headers)

        self.logger = get_logger(
            self.__class__.__name__
        )

    def initialize(self) -> None:

        self.logger.info(
            "Initializing NSE Home Page session"
        )

        response = self.session.get(
            self.base_url,
            timeout=self.timeout
        )

        self.logger.info(
            "Initializing NSE option chain session"
        )

        self.session.get(
            f"{self.base_url}/option-chain",
            timeout=self.timeout
        )

        self.logger.info(
            "NSE session initialized successfully"
        )

        response.raise_for_status()

       

    def get_session(self) -> Session:

        return self.session