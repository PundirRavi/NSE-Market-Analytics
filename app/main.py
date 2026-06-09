from core.logging_config import configure_logging

configure_logging()

from core.logger import logger

from ingestion.clients.nse_client import NSEClient

from infra.exceptions.api_exceptions import APIError


def main():

    try:

        client = NSEClient()

        data = client.get_market_status()

        logger.info("Market status retrieved successfully | markets=%s",
                len(data.marketState)
                )

        for market in data.marketState:
            logger.info(
                    "%s | %s ",
                    market.market,
                    market.marketStatus
                    )
    except APIError as exc:

        logger.error(f"API Failed: {exc}")


if __name__ == "__main__":
    main()