from src.streaming.event_factory import EventFactory
from src.streaming.topics import Topics
from src.utils.logger import get_logger

class OptionChainJob:

    def __init__(
            self,
            service,
            symbols, 
            producer
    ) -> None:
        
        self.service=service
        self.symbols=symbols
        self.producer=producer

        self.logger=get_logger(self.__class__.__name__)

    def run(self):

        self.logger.info(
            "Starting OptionChainJob"
        )

        results={}

        for symbol in self.symbols:

            self.logger.info(
                "Processing %s",
                symbol
            )

            results[symbol] = (
                self.service
                .fetch_option_chain(
                    symbol
                )
            )

            event = EventFactory.create(
                source="NSE",
                dataset="option-chain",
                payload=results[symbol].model_dump(
                    mode="json"
                ),
            )

            self.producer.send(
                topic=Topics.OPTION_CHAIN,
                event=event,
            )

        self.logger.info(
                "Completed OptionChainJob"
        )

        return results