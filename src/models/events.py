from pydantic import BaseModel, Field
from datetime import datetime


class MarketStatusEvent(BaseModel):
    """
    Standard event wrapper for streaming systems.

    WHY this exists:
    - Adds metadata around raw payload
    - Enables schema evolution
    - Supports Kafka consumers downstream
    """

    event_name: str = "market_status"

    # IMPORTANT: store as ISO string, not datetime object
    event_time: str = Field(default_factory=lambda: datetime.now().isoformat())
    schema_version: str = "1.0"

    source: str = "nse"

    payload: dict