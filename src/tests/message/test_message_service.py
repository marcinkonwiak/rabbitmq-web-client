from dataclasses import asdict

from pika.delivery_mode import DeliveryMode
from sqlalchemy.orm import Session

from src.message.models import Message
from src.message.schemas import MessageUpdate
from src.message.service import create, delete, get, get_without_parents, update


def test_get(db_session: Session, message: Message):
    assert get(db_session, message.id).id == message.id


def test_create(db_session: Session):
    message = create(db_session)
    assert message.id is not None
    assert message.name == "New Message"

    message = create(db_session, False)
    assert message.id is None
    assert message.name == "New Message"


def test_update(db_session: Session, message: Message):
    update_data = MessageUpdate(
        name="Test name",
        body="Test body",
        inherit_settings=True,
        amqp_url="Test amqp_url",
        routing_key="Test routing_key",
        exchange="Test exchange",
        content_type="Test content_type",
        content_encoding="Test content_encoding",
        headers="test headers",
        delivery_mode=DeliveryMode.Transient,
        priority=1,
        correlation_id="Test correlation_id",
        reply_to="Test reply_to",
        expiration="Test expiration",
        amqp_message_id="Test amqp_message_id",
        timestamp="1577833200",
        type="Test type",
        user_id="Test user_id",
        app_id="Test app_id",
        cluster_id="Test cluster_id",
    )

    message = update(db_session, message, asdict(update_data))

    assert message.name == update_data.name
    assert message.body == update_data.body
    assert message.inherit_settings == update_data.inherit_settings
    assert message.amqp_url == update_data.amqp_url
    assert message.routing_key == update_data.routing_key
    assert message.exchange == update_data.exchange
    assert message.content_type == update_data.content_type
    assert message.content_encoding == update_data.content_encoding
    assert message.headers == update_data.headers
    assert message.delivery_mode == update_data.delivery_mode
    assert message.priority == update_data.priority
    assert message.correlation_id == update_data.correlation_id
    assert message.reply_to == update_data.reply_to
    assert message.expiration == update_data.expiration
    assert message.amqp_message_id == update_data.amqp_message_id
    assert message.timestamp == update_data.timestamp
    assert message.type == update_data.type
    assert message.user_id == update_data.user_id
    assert message.app_id == update_data.app_id
    assert message.cluster_id == update_data.cluster_id


def test_delete(db_session: Session, message: Message):
    message = db_session.get(Message, message.id)
    delete(db_session, message)  # type: ignore
    assert db_session.get(Message, message.id) is None


def test_get_without_parents(db_session: Session, message: Message):
    messages = get_without_parents(db_session)
    assert len(messages) == 0

    message.collection = None
    db_session.commit()

    messages = get_without_parents(db_session)
    assert len(messages) == 1
