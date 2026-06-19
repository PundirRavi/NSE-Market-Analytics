from src.streaming.event_factory import EventFactory
from src.streaming.topics import Topics
from src.utils.logger import get_logger

class MarketStatusJob:

    def __init__(
        self,
        guard,
        service,
        producer
    ) -> None:
        
        self.guard = guard
        self.service = service
        self.producer=producer

        self.logger = get_logger(
            self.__class__.__name__
        )

    def run(self) -> None:

        try:

            self.logger.info("Starting MarketStatusJob")

            if not self.guard.can_run_market_jobs():

                self.logger.info(
                    "Skipping MarketStatusJob because market is closed"
                )

                return
            
            self.logger.info(
                "Market open. Fetching market status"
            )
            
            status = (
                self.service
                .fetch_market_status()
            )


            event = EventFactory.create(
                source="NSE",
                dataset="market_status",
                payload=status.model_dump(
                    mode="json"
                ),
            )

            self.producer.send(
                topic=Topics.MARKET_STATUS,
                event=event,
            )

            self.logger.info(
                "Publishing Market Status event to Kafka"
            )

            return status

        except Exception as exc:

            self.logger.exception("Market Status Job failed due to: %s", exc)

            raise