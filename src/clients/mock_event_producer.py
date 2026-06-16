import json
from pathlib import Path

from src.utils.logger import get_logger
from src.clients.event_producer_interface import EventProducerInterface


class MockEventProducer(EventProducerInterface):
    """
    Local replacement for Kafka.

    WHY this exists:
    - Allows development without Kafka installed
    - Simulates event publishing
    - Stores events locally for debugging
    """

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)
        self.events_file = Path("data/mock_kafka_events.jsonl")
        self.events_file.parent.mkdir(parents=True, exist_ok=True)

    def send(self, topic: str, key: str, value: dict) -> None:
        event = {
            "topic": topic,
            "key": key,
            "value": value,
        }

        # SAFE serialization
        serialized = json.dumps(event, default=str)

        with open(self.events_file, "a", encoding="utf-8") as f:
            f.write(serialized + "\n")

        self.logger.info(
            "Mock event published -> topic=%s key=%s",
            topic,
            key,
        )

    def flush(self) -> None:
        self.logger.info("Mock flush (no-op)")