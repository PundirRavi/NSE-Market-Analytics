from src.utils.logger import get_logger
import time

class StreamRunner:

    def __init__(
        self,
        job_execute_fn,
        market_guard,
        interval_seconds=10,
        market_check_interval=6,
    ):
        self.logger = get_logger(self.__class__.__name__)
        self.job_execute_fn = job_execute_fn
        self.market_guard = market_guard

        self.interval_seconds = interval_seconds
        self.market_check_interval = market_check_interval

        self._running = True
        self._cycle_count = 0

    def start(self):

        while self._running:

            # Check market state periodically
            if self._cycle_count % self.market_check_interval == 0:
                if not self.market_guard.is_market_open():
                    self.logger.info("Market closed → sleeping")
                    time.sleep(30)
                    continue

            try:
                self.job_execute_fn()

            except Exception as e:
                self.logger.exception("Cycle failed")

            self._cycle_count += 1
            time.sleep(self.interval_seconds)