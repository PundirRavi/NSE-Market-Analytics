from pydantic import BaseModel


class MarketState(BaseModel):
    market: str
    marketStatus: str
    tradeDate: str
    index: str
    last: float | str | None = None
    variation: float | str | None = None
    percentChange: float | str | None = None
    marketStatusMessage: str


class MarketStatusResponse(BaseModel):
    marketState: list[MarketState]