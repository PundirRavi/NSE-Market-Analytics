import json
from datetime import datetime
from pathlib import Path

from ingestion.storage.storage_interface import StorageInterface


class LocalStorage(StorageInterface):

    RAW_DATA_PATH = Path("data/raw")

    def save_json(
        self,
        dataset: str,
        payload: dict
    ) -> str:

        now = datetime.now()

        year_path = f"year={now.year}"
        month_path = f"month={now.month:02d}"
        day_path = f"day={now.day:02d}"

        target_dir = (
            self.RAW_DATA_PATH
            / dataset
            / year_path
            / month_path
            / day_path
        )

        target_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_name = (
            f"{dataset}_"
            f"{now.strftime('%Y%m%d_%H%M%S')}.json"
        )

        file_path = target_dir / file_name

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                payload,
                file,
                indent=4
            )

        return str(file_path)