import json

from src.streaming.event_factory import EventFactory
from src.streaming.serializer import EventSerializer


def test_serialize_event_success():

    payload = {
        "marketStatus": "Open"
    }

    event = EventFactory.create(
        source="NSE",
        dataset="market_status",
        payload=payload,
    )

    serialized = EventSerializer.serialize(
        event
    )

    assert isinstance(
        serialized,
        str,
    )

    data = json.loads(
        serialized
    )

    assert data["source"] == "NSE"

    assert data["dataset"] == "market_status"

    assert data["payload"] == payload

    assert "event_id" in data

    assert "event_time" in data