from src.streaming.kafka_producer import KafkaProducer
from src.models.config.kafka_config import KafkaConfig

class ProducerFactory:

    @staticmethod
    def create(
        config: KafkaConfig
    ) -> KafkaProducer:


        return KafkaProducer(config)