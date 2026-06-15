import logging
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    Central application configuration loaded from environment variables.
    """
    # =====================
    # Core App Settings
    # =====================
    ENV: str = "dev"
    APP_NAME: str = "elt-pipeline"
    DEBUG: bool = False

    # =====================
    # Azure / Storage
    # =====================
    ADLS_CONNECTION_STRING: str = ""
    BRONZE_CONTAINER: str = "bronze"
    SILVER_CONTAINER: str = "silver"
    GOLD_CONTAINER: str = "gold"

    # =====================
    # Optional Settings
    # =====================
    LOG_LEVEL: str = "INFO"

    # =====================
    # Pydantic Config
    # =====================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Singleton settings loader.
    Ensures settings are loaded only once per application lifecycle.
    """
    try:
        settings = Settings()
        logger.info("Settings loaded successfully for ENV=%s", settings.ENV)
        return settings
    except Exception as e:
        logger.exception("Failed to load application settings")
        raise