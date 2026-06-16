
from src.utils.logger import get_logger


class MarketStateGuard:
    """
    Central policy layer for NSE execution decisions.

    WHY this exists:
    - Avoid duplicating "market open/close" logic across jobs
    - Centralize trading calendar rules
    - Future extension: holidays, pre-market, post-market
    """

    def __init__(self, calendar_service) -> None:

        self.calendar_service = calendar_service
        self.logger = get_logger(self.__class__.__name__)

    def can_run_market_jobs(self) -> bool:
        """
        Checks NSE Capital Market status.
        Returns True if market is OPEN.
        """

        is_open = (
            self.calendar_service
            .is_market_open()
        )

        self.logger.info(
            "Market Open = %s",
            is_open
        )

        return is_open