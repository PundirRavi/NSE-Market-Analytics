from pydantic import BaseModel

class OptionLeg(BaseModel):

    strikePrice: int 
    openInterest: int 
    changingOpenInterest: int 
    impliedVolatility: float | None = None
    lastPrice: float | None = None 
    totalTradedVolume: int | None = None


class OptionStrike(BaseModel):
    strikePrice: int 
    CE: OptionLeg | None = None
    PE: OptionLeg | None = None

class OptionChainRecords(BaseModel):
    expiryDates: list[str]
    data: list[OptionStrike]

class OptionChainResponse(BaseModel):
    records: OptionChainRecords