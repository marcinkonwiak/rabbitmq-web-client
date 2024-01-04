from dataclasses import dataclass
from datetime import datetime

from fastapi import Form
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
    amqp_message_id: str | None
    timestamp: datetime | None
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
    consumer_tag: str | None = Form(default=None)
    delivery_tag: int | None = Form(default=None)
    redelivered: bool | None = Form(default=None)

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
    timestamp: datetime | None = Form(default=None)
    type: str | None = Form(default=None)
    user_id: str | None = Form(default=None)
    app_id: str | None = Form(default=None)
    cluster_id: str | None = Form(default=None)
