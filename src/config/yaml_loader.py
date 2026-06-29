from functools import lru_cache
from pathlib import Path
import yaml

from src.models.config.config_models import AppConfig


def _load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


@lru_cache
def load_config() -> AppConfig:

    base_path = Path(__file__).parent / "yaml"

    nse_config = _load_yaml(base_path / "nse.yaml")
    kafka_config = _load_yaml(base_path / "kafka.yaml")

    merged_config = {
        "nse": nse_config,
        "kafka": kafka_config
    }

    return AppConfig.model_validate(merged_config)