from core.logger import logger
from datetime import datetime


class MarketStatusPipeline:

    def __init__(self, client, storage):
        self.client = client
        self.storage = storage

    def run(self):

        try:
            logger.info("MarketStatusPipeline started")

            raw = self.client.get_market_status().model_dump()

            payload = {
                "source": "nse",
                "dataset": "market_status",
                "ingestion_time": str(datetime.utcnow()),
                "data": raw
            }

            path = self.storage.save_json(
                dataset="market_status",
                payload=payload
            )

            logger.info("Pipeline success | path=%s", path)

            return {
                "status": "success",
                "path": path
            }

        except Exception as exc:
            logger.exception("Pipeline failed")
            raise