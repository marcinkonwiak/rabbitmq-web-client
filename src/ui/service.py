from sqlalchemy import select, union
from sqlalchemy.orm import Session

from src.collection.models import Collection
from src.message.models import Message


def get_next_item_weight(
    db_session: Session,
    collection_id: int | None,
    weight: float | None,
    exclude_id: int | None = None,
) -> float | None:
    message_query = select(Message.weight).where(
        Message.id != exclude_id,
        Message.collection_id == collection_id,
    )
    collection_query = select(Collection.weight).where(Collection.id != exclude_id)

    if weight is not None:
        message_query = message_query.where(Message.weight > weight)
        collection_query = collection_query.where(Collection.weight > weight)

    query = union(message_query, collection_query).order_by("weight").limit(1)

    return db_session.execute(query).scalars().first()
