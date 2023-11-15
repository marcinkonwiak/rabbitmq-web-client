import pika

from message.models import Message


def publish_message(message: Message):
    connection = pika.BlockingConnection(
        pika.URLParameters(message.amqp_url)
    )
    channel = connection.channel()

    channel.basic_publish(
        exchange=message.exchange,
        routing_key=message.queue,
        body=message.body.encode(),
        properties=pika.BasicProperties(
            headers={
                "todo": "todo",
            }
        )
    )
