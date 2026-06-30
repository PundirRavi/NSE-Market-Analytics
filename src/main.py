
import json

from src.cache.ttl_cache import TTLCache
from src.sessions.nse_session import NSESession

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

from src.clients.option_chain_client import (
    OptionChainClient
)

from src.services.option_chain_service import (
    OptionChainService
)

from src.jobs.option_chain_job import (
    OptionChainJob
)

from src.streaming.producer_factory import ProducerFactory


def build_application():

    config = load_config()

    nse_session = NSESession(
                base_url=config.nse.base_url,
                headers=config.nse.headers,
                timeout=config.nse.timeout
    )

    nse_session.initialize()

    session = nse_session.get_session()

    # ✅ Kafka Producer creation
    producer=ProducerFactory.create(
        config.kafka
    )

    client = MarketStatusClient(
        config=config.nse,
        session=session
    )

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

    market_job  = MarketStatusJob(
        guard=guard,
        service=service,
        producer=producer
    )

    #option chain 

    option_client = OptionChainClient(
            config.nse,
            session=session
    )

    option_service = OptionChainService(
        option_client,
        cache
    )

    option_job = OptionChainJob(
        service=option_service,
        symbols=config.nse.datasets.option_chain.symbols,
        producer=producer
    )


    return market_job, option_job, producer


def main():

    market_job, option_job, kafka_producer = build_application()

    try:
        """#market status job execution
        market_result = market_job.run()

        if market_result is not None:
            print(market_result.model_dump_json(indent=2))
        else:
            print("No result returned from  Market Status Job")"""

        #option chain job execution
        option_result = option_job.run()

        if option_result is not None:
            print(json.dumps(option_result, indent=2))
        else:
            print("No result returned from  option chain Job") 

    finally:
        # ✅ flush Kafka before shutdown
        kafka_producer.flush()      