from src.notifications.notification_interface import NotificationInterface
from src.utils.logger import get_logger


class ConsoleNotification(NotificationInterface):

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def send(self, title: str, message: str) -> None:
        self.logger.warning("NOTIFICATION: %s - %s", title, message)