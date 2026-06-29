from pydantic import BaseModel, Field
from src.models.config.kafka_config import KafkaConfig

class DatasetConfig(BaseModel):
    endpoint: str
    poll_interval_sec: int


class OptionChainConfig(DatasetConfig):
    symbols: list[str] = Field(default_factory=list)

class DatasetCollection(BaseModel):
    market_status: DatasetConfig
    option_chain: OptionChainConfig

class NSEConfig(BaseModel):
    base_url: str
    timeout: int
    headers: dict[str, str]
    datasets: DatasetCollection
    


class AppConfig(BaseModel):
    nse: NSEConfig
    kafka: KafkaConfig