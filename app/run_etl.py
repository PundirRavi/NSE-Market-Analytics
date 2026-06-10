from core.logging_config import configure_logging
configure_logging()

from core.logger import logger
from core.config.settings import get_settings

from ingestion.clients.nse_client import NSEClient
from storage.adls_storage import ADLSStorage
from ingestion.jobs.market_status_job import MarketStatusPipeline

from core.config.settings import get_settings

settings = get_settings()

def main():

    settings = get_settings()
    ADLS_CONNECTION_STRING=settings.ADLS_CONNECTION_STRING

    logger.info("Starting ETL | env=%s", settings.ENV)

    client = NSEClient()

    logger.info(
    "ADLS conn present=%s",
    bool(ADLS_CONNECTION_STRING)
)

    logger.info(
        "ADLS conn starts_with=%s",
        ADLS_CONNECTION_STRING[:30]
        if ADLS_CONNECTION_STRING
        else "NONE"
)
    
    storage = ADLSStorage(
        connection_string=ADLS_CONNECTION_STRING,
        container=settings.BRONZE_CONTAINER
    )

    pipeline = MarketStatusPipeline(
        client=client,
        storage=storage
    )

    result = pipeline.run()

    logger.info("ETL completed | path=%s", result["path"])


if __name__ == "__main__":
    main()