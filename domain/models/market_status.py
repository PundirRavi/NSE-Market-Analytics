from typing import List, Optional

from pydantic import BaseModel


class MarketState(BaseModel):
    market: str
    marketStatus: str
    tradeDate: Optional[str] = None

    index: Optional[str] = None
    marketStatusMessage: Optional[str] = None


class MarketStatusResponse(BaseModel):
    marketState: List[MarketState]