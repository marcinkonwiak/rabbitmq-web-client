from pika.delivery_mode import DeliveryMode
from pydantic import conint
from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.dialects.sqlite import JSON

PrimaryKey = conint(gt=0, lt=2147483647)


class SettingsMixin:
    amqp_url = Column(String)

    # Routing details
    routing_key = Column(String)
    exchange = Column(String)

    # Message properties
    content_type = Column(String)
    content_encoding = Column(String)
    headers = Column(JSON)
    delivery_mode = Column(Enum(DeliveryMode))
    priority = Column(Integer)
    correlation_id = Column(String)
    reply_to = Column(String)
    expiration = Column(String)
    amqp_message_id = Column(String)
    timestamp = Column(String(length=10))
    type = Column(String)
    user_id = Column(String)
    app_id = Column(String)
    cluster_id = Column(String)


class ItemSettingsMixin(SettingsMixin):
    inherit_settings = Column(Boolean, default=False, nullable=False)
