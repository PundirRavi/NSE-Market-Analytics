import json

from src.exceptions.custom_exceptions import SerializationException
from src.models.events import Event
from src.utils.logger import get_logger


class EventSerializer:
    """
    Serializes Event objects into JSON strings
    suitable for Kafka publishing.
    """

    logger = get_logger("EventSerializer")

    @staticmethod
    def serialize(
        event: Event,
    ) -> str:

        try:

            EventSerializer.logger.info(
                "Serializing event | Dataset=%s | Symbol=%s",
                event.dataset,
                event.symbol,
            )

            serialized = json.dumps(
                event.model_dump(
                    mode="json",
                )
            )

            EventSerializer.logger.info(
                "Event serialized successfully."
            )

            return serialized

        except Exception as exc:

            EventSerializer.logger.exception(
                "Failed to serialize event."
            )

            raise SerializationException(
                "Unable to serialize event."
            ) from exc