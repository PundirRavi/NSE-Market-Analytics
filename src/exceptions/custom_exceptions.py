class NSEPlatformException(Exception):
    """Base exception for the application."""


class ConfigurationException(NSEPlatformException):
    """Raised when configuration is invalid."""


class NSEApiException(NSEPlatformException):
    """Raised when NSE API calls fail."""


class StorageException(NSEPlatformException):
    """Raised when storage operations fail."""


class NotificationException(NSEPlatformException):
    """Raised when notification delivery fails."""

class ClientException(NSEPlatformException):
    """Raised when an external client operation fails."""