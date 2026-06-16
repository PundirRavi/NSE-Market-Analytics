from src.cache.ttl_cache import TTLCache

from src.clients.market_status_client import (
    MarketStatusClient
)

from src.config.yaml_loader import (
    load_config
)

from src.services.market_status_service import (
    MarketStatusService
)

from src.services.trading_calendar_service import (
    TradingCalendarService
)

from src.guards.market_state_guard import (
    MarketStateGuard
)

from src.jobs.market_status_job import (
    MarketStatusJob
)


def build_application():

    config = load_config()


    client = MarketStatusClient(config=config.nse)

    cache = TTLCache(
        ttl_seconds=30
    )

    service = MarketStatusService(
        client=client,
        cache=cache
    )

    calendar_service = (
        TradingCalendarService()
    )

    guard = MarketStateGuard(
        calendar_service
    )

    job = MarketStatusJob(
        guard=guard,
        service=service
    )

    return job


def main():

    job = build_application()

    result = job.run()

    print(result)
