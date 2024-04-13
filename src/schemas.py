from dataclasses import dataclass

from fastapi import Form
from pika.delivery_mode import DeliveryMode


class SettingsReadMixin:
    amqp_url: str | None

    # Routing details
    routing_key: str | None
    exchange: str | None

    # Message properties
    content_type: str | None
    content_encoding: str | None
    headers: str | None
    delivery_mode: DeliveryMode | None
    priority: int | None
    correlation_id: str | None
    reply_to: str | None
    expiration: str | None
    amqp_message_id: str | None
    timestamp: str | None
    type: str | None
    user_id: str | None
    app_id: str | None
    cluster_id: str | None


@dataclass
class SettingsFormMixin:
    amqp_url: str | None = Form(default=None)

    # Routing details
    routing_key: str | None = Form(default=None)
    exchange: str | None = Form(default=None)

    # Message properties
    content_type: str | None = Form(default=None)
    content_encoding: str | None = Form(default=None)
    headers: str | None = Form(default=None)
    delivery_mode: DeliveryMode | None = Form(default=None)
    priority: int | None = Form(default=None)
    correlation_id: str | None = Form(default=None)
    reply_to: str | None = Form(default=None)
    expiration: str | None = Form(default=None)
    amqp_message_id: str | None = Form(default=None)
    timestamp: str | None = Form(default=None, max_length=10)
    type: str | None = Form(default=None)
    user_id: str | None = Form(default=None)
    app_id: str | None = Form(default=None)
    cluster_id: str | None = Form(default=None)
