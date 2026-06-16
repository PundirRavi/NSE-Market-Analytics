import json
from datetime import datetime
from pathlib import Path

from src.storage.storage_interface import StorageInterface
from src.utils.logger import get_logger


class LocalStorage(StorageInterface):

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def save_json(
        self,
        dataset: str,
        payload: dict,
    ) -> str:

        now = datetime.now()

        folder = (
            Path("data")
            / "raw"
            / dataset
            / str(now.year)
            / f"{now.month:02d}"
            / f"{now.day:02d}"
        )

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = folder / f"{now.strftime('%H%M%S')}.json"

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                payload,
                file,
                indent=2,
            )

        self.logger.info(
            "Saved file: %s",
            file_path,
        )

        return str(file_path)