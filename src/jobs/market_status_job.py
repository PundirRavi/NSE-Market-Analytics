
from src.utils.logger import get_logger

class MarketStatusJob:

    def __init__(
        self,
        guard,
        service
    ) -> None:
        
        self.guard = guard
        self.service = service

        self.logger = get_logger(
            self.__class__.__name__
        )

    def run(self) -> None:

        try:
            if not self.guard.can_run_market_jobs():

                self.logger.info(
                    "Market closed. Skipping."
                )

                return
            
            status = (
                self.service
                .fetch_market_status()
            )

            self.logger.info(
                "Fetched market status"
            )

            return status

        except Exception as exc:

            self.logger.exception("Job failed due to :", exc)

            