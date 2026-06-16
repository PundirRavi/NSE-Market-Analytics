from pydantic import BaseModel


class Quote(BaseModel):
    symbol: str
    last_price: float