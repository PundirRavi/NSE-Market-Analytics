from functools import lru_cache
from pathlib import Path

import yaml

from src.models.config_models import AppConfig


@lru_cache
def load_config() -> AppConfig:
    
    config_path = Path(__file__).parent / "yaml" / "nse.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    return AppConfig.model_validate(config_data)