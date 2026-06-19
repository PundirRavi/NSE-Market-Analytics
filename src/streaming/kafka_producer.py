from confluent_kafka import Producer
from src.models.config.kafka_config import KafkaConfig
from src.exceptions.custom_exceptions import StreamingException
from src.models.events import Event
from src.streaming.serializer import EventSerializer
from src.utils.logger import get_logger


class KafkaProducer:

    def __init__(
        self,
        config: KafkaConfig
    ):
        bootstrap_servers = ",".join(config.bootstrap_servers)

        # ✅  create confluent producer
        self.producer = Producer({
            "bootstrap.servers": bootstrap_servers,
            "client.id": config.client_id
        })

        self.logger = get_logger(
            self.__class__.__name__
        )

        self.logger.info(
            "Kafka Producer initialized."
        )

    def _delivery_report(
            self,
            err,
            msg,
    ) -> None:

        if err:

            self.logger.error(
                "Message delivery failed: %s",
                err,
            )

        else:

            self.logger.info(
                (
                    "Message delivered | "
                    "Topic=%s | "
                    "Partition=%s | "
                    "Offset=%s"
                ),
                msg.topic(),
                msg.partition(),
                msg.offset(),
            )

    def send(
        self,
        topic: str,
        event: Event,
    ) -> None:

        try:

            self.logger.info(
                "Publishing event | Topic=%s | Dataset=%s | Symbol=%s",
                topic,
                event.dataset,
                event.symbol,
            )

            message = EventSerializer.serialize(
                event
            )

            self.producer.produce(
                topic=topic,
                value=message,
                callback=self._delivery_report,
            )

        except Exception as exc:

            self.logger.exception(
                "Kafka publish failed.", exc
            ) 

            raise StreamingException(
                "Unable to publish event."
            ) from exc
        
    def flush(self):
        """Call this on shutdown only"""
        self.producer.flush()

    def close(self):
        """Alias for cleanup"""
        self.producer.flush()