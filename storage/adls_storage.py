import json
from datetime import datetime
from azure.storage.blob import BlobServiceClient
from core.logger import logger


class ADLSStorage:

    def __init__(self, connection_string: str, container: str = "bronze"):
        try:
            self.blob_service_client = BlobServiceClient.from_connection_string(
                connection_string
            )
            self.container = container

            logger.info("ADLS client initialized | container=%s", container)

        except Exception as exc:
            logger.exception("Failed to initialize ADLS client")
            raise RuntimeError("ADLS initialization failed") from exc

    def save_json(self, dataset: str, payload: dict) -> str:

        try:
            now = datetime.utcnow()

            blob_path = (
                f"bronze/{dataset}/"
                f"year={now.year}/month={now.month}/day={now.day}/"
                f"{now.strftime('%Y%m%d_%H%M%S')}.json"
            )

            logger.info("Preparing blob upload | path=%s", blob_path)

            blob_client = self.blob_service_client.get_blob_client(
                container=self.container,
                blob=blob_path
            )

            blob_client.upload_blob(
                json.dumps(payload, indent=2),
                overwrite=True
            )

            logger.info("Upload successful | dataset=%s | path=%s", dataset, blob_path)

            return blob_path

        except Exception as exc:
            logger.exception(
                "ADLS upload failed | dataset=%s",
                dataset
            )
            raise RuntimeError("Failed to upload data to ADLS") from exc