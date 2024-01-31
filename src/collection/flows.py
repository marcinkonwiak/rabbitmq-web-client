from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.ui.flows import move_sidebar_item
from src.ui.service import get_next_item_weight

from .models import Collection
from .schemas import CollectionList
from .service import get, get_all


def get_collection_list(db_session: Session) -> CollectionList:
    collections = get_all(db_session)

    for collection in collections:
        collection.messages.sort(key=lambda m: m.weight)

    return CollectionList(collections=collections)


def get_collection_from_id(db_session: Session, collection_id: int) -> Collection:
    if not (collection := get(db_session, collection_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A collection with this id does not exist."}],
        )

    return collection


def move(
    db_session: Session,
    collection: Collection,
    prev_item_weight: float | None,
):
    next_item = get_next_item_weight(
        db_session,
        None,
        prev_item_weight,
        exclude_id=collection.id,
    )
    move_sidebar_item(collection, next_item, prev_item_weight)

    db_session.commit()
