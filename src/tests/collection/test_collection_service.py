from dataclasses import asdict

from pika.delivery_mode import DeliveryMode
from sqlalchemy.orm import Session

from src.collection.models import Collection
from src.collection.schemas import CollectionUpdate
from src.collection.service import create, delete, get, get_all, update


def test_get(db_session: Session, collection: Collection):
    assert get(db_session, collection.id).id == collection.id


def test_get_all(db_session: Session, collection: Collection):
    collections = get_all(db_session)
    assert collection in collections


def test_create(db_session: Session):
    collection = create(db_session)
    assert collection.id is not None
    assert collection.name == "New Collection"


def test_update(db_session: Session, collection: Collection):
    update_data = CollectionUpdate(
        name="Test name",
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
    collection = update(db_session, collection, asdict(update_data))

    assert collection.name == update_data.name
    assert collection.amqp_url == update_data.amqp_url
    assert collection.routing_key == update_data.routing_key
    assert collection.exchange == update_data.exchange
    assert collection.content_type == update_data.content_type
    assert collection.content_encoding == update_data.content_encoding
    assert collection.headers == update_data.headers
    assert collection.delivery_mode == update_data.delivery_mode
    assert collection.priority == update_data.priority
    assert collection.correlation_id == update_data.correlation_id
    assert collection.reply_to == update_data.reply_to
    assert collection.expiration == update_data.expiration
    assert collection.amqp_message_id == update_data.amqp_message_id
    assert collection.timestamp == update_data.timestamp
    assert collection.type == update_data.type
    assert collection.user_id == update_data.user_id
    assert collection.app_id == update_data.app_id
    assert collection.cluster_id == update_data.cluster_id


def test_delete(db_session: Session, collection: Collection):
    delete(db_session, collection)
    assert get(db_session, collection.id) is None
