from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any 
from uuid import UUID

class Event(BaseModel):
    """
    Standard event envelope published to Kafka.

    Every dataset (market status, option chain, quotes, etc.)
    is wrapped inside this model.
    """
    event_id: UUID = Field(
        description="Unique identifier for the event."
    )

    event_time: datetime = Field(
        description="UTC timestamp when the event was created."
    )

    source: str = Field(
        description="Source system generating the event."
    )

    dataset: str = Field(
        description="Dataset name."
    )

    symbol: str | None = Field(
        default=None,
        description="Trading symbol if applicable."
    )

    payload: Any = Field(
        description="Validated dataset payload."
    )

    