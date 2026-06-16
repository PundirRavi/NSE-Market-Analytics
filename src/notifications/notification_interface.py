from abc import ABC, abstractmethod


class NotificationInterface(ABC):

    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass