from sqlalchemy import select, union
from sqlalchemy.orm import Session

from src.collection.models import Collection
from src.message.models import Message

from .schemas import SidebarItem


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


def fix_sidebar_item_weights(db_session: Session):
    """
    In case float precision isn't enough and weights of two items end up being the same.
    """
    messages = db_session.execute(select(Message).order_by("weight")).scalars().all()
    collections = (
        db_session.execute(select(Collection).order_by("weight")).scalars().all()
    )

    sidebar_items: list[SidebarItem] = []
    sidebar_items.extend(collections)
    sidebar_items.extend(messages)
    sidebar_items.sort(key=lambda s: s.weight)

    for i, item in enumerate(sidebar_items):
        item.weight = i

    db_session.commit()
