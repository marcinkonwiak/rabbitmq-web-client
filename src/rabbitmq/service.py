import pika

from src.message.models import Message


def publish_message(message: Message):
    connection = pika.BlockingConnection(
        pika.URLParameters(get_property_value(message, "amqp_url") or "")
    )
    channel = connection.channel()

    channel.basic_publish(
        exchange=get_property_value(message, "exchange") or "",
        routing_key=get_property_value(message, "routing_key") or "",
        body=(message.body or "").encode(),
        properties=get_properties(message),
    )


def get_property_value(message, key):
    return (
        getattr(message.collection, key)
        if message.inherit_settings and message.collection
        else getattr(message, key)
    )


def get_properties(message: Message) -> pika.BasicProperties:
    properties = {
        key: get_property_value(message, key)
        for key in [
            "content_type",
            "content_encoding",
            "headers",
            "delivery_mode",
            "priority",
            "correlation_id",
            "reply_to",
            "expiration",
            "amqp_message_id",
            "timestamp",
            "type",
            "user_id",
            "app_id",
            "cluster_id",
        ]
    }
    properties["message_id"] = properties.pop("amqp_message_id")

    return pika.BasicProperties(**properties)
