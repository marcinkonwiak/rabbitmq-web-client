from datetime import datetime

from pika.delivery_mode import DeliveryMode


class SettingsReadMixin:
    amqp_url: str | None

    # Routing details
    routing_key: str | None
    exchange: str | None
    consumer_tag: str | None
    delivery_tag: int | None
    redelivered: bool | None

    # Message properties
    content_type: str | None
    content_encoding: str | None
    headers: str | None
    delivery_mode: DeliveryMode | None
    priority: int | None
    correlation_id: str | None
    reply_to: str | None
    expiration: str | None
    message_id: str | None
    timestamp: datetime | None
    type: str | None
    user_id: str | None
    app_id: str | None
    cluster_id: str | None
