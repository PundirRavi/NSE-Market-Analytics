from datetime import datetime, timezone
from uuid import uuid4

from src.exceptions.custom_exceptions import EventCreationException
from src.models.events import Event
from src.utils.logger import get_logger


class EventFactory:
    """
    Factory responsible for creating Event objects.
    """

    logger = get_logger("EventFactory")

    @staticmethod
    def create(
        *,
        source: str,
        dataset: str,
        payload,
        symbol: str | None = None,
    ) -> Event:

        try:

            EventFactory.logger.info(
                "Creating event | Dataset=%s | Symbol=%s",
                dataset,
                symbol,
            )

            event = Event(
                event_id=uuid4(),
                event_time=datetime.now(timezone.utc),
                source=source,
                dataset=dataset,
                symbol=symbol,
                payload=payload,
            )

            EventFactory.logger.info(
                "Event created successfully | Event ID=%s",
                event.event_id,
            )

            return event

        except Exception as exc:

            EventFactory.logger.exception(
                "Failed to create event."
            )

            raise EventCreationException(
                "Unable to create streaming event."
            ) from exc