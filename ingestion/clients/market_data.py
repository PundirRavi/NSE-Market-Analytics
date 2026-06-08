from pydantic import BaseModel


class MarketData(BaseModel):
    symbol: str
    timestamp: str
    price: float