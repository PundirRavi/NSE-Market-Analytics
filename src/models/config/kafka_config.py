from pydantic import BaseModel, ConfigDict


class KafkaProducerConfig(BaseModel):

    model_config = ConfigDict(frozen=True)

    acks: str

    retries: int

    compression_type: str

    linger_ms: int

    batch_size: int

    enable_idempotence: bool

class KafkaTopicsConfig(BaseModel):

    model_config = ConfigDict(frozen=True)

    market_status: str

    option_chain: str

class KafkaConfig(BaseModel):

    model_config = ConfigDict(frozen=True)

    bootstrap_servers: list[str]

    client_id: str

    producer: KafkaProducerConfig

    topics: KafkaTopicsConfig