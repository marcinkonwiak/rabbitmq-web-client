from pika.delivery_mode import DeliveryMode
from pydantic import conint
from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String
from sqlalchemy.dialects.sqlite import JSON

from src.database.core import Base

PrimaryKey = conint(gt=0, lt=2147483647)


class SettingsMixin:
    amqp_url = Column(String)

    # Routing details
    routing_key = Column(String)
    exchange = Column(String)
    consumer_tag = Column(String)
    delivery_tag = Column(Integer)
    redelivered = Column(Boolean)

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
    timestamp = Column(DateTime)
    type = Column(String)
    user_id = Column(String)
    app_id = Column(String)
    cluster_id = Column(String)


class ItemSettingsMixin(SettingsMixin):
    inherit_settings = Column(Boolean, default=True, nullable=False)


class GlobalSettings(Base, SettingsMixin):
    __tablename__ = "global_settings"

    id = Column(Integer, primary_key=True)
