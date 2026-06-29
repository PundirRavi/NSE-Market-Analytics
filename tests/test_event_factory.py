from src.streaming.event_factory import EventFactory

def test_create_event_success():

    payload={
        "marketStatus": "Open"
    }

    event = EventFactory.create(
        source="NSE",
        dataset="market_status",
        payload=payload,
    )

    assert event.source == "NSE"
    assert event.dataset == "market_status"
    assert event.payload == payload

    assert event.symbol is None

    assert event.event_id is not None

    assert event.event_time is not None

def test_create_event_with_symbol():

    payload = {
        "price": 25000
    }

    event = EventFactory.create(
        source="NSE",
        dataset="option_chain",
        symbol="NIFTY",
        payload=payload,
    )

    assert event.symbol == "NIFTY"


