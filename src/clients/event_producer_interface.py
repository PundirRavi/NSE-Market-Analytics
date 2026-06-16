from abc import ABC, abstractmethod


class EventProducerInterface(ABC):

    @abstractmethod
    def send(self, topic: str, key: str, value: dict) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass