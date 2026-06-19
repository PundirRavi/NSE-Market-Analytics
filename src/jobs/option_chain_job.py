from src.utils.logger import get_logger

class OptionChainJob:

    def __init__(
            self,
            service,
            symbols
    ) -> None:
        
        self.service=service
        self.symbols=symbols

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

            self.logger.info(
                "Completed OptionChainJob"
            )

            return results