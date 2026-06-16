from pydantic import BaseModel


class DatasetConfig(BaseModel):
    endpoint: str
    poll_interval_sec: int


class NSEConfig(BaseModel):
    base_url: str
    timeout: int
    headers: dict[str, str]
    datasets: dict[str, DatasetConfig]


class AppConfig(BaseModel):
    nse: NSEConfig