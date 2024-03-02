from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Collection


def get(db_session: Session, collection_id: int) -> Collection | None:
    return db_session.get(Collection, collection_id)


def get_all(db_session: Session) -> Sequence[Collection]:
    return db_session.execute(select(Collection)).scalars().all()


def create(db_session: Session, commit: bool = True) -> Collection:
    collection = Collection(name="New Collection")
    db_session.add(collection)
    if commit:
        db_session.commit()

    return collection


def update(
    db_session: Session,
    collection: Collection,
    update_data: dict,
) -> Collection:
    collection_data = collection.dict()

    for field in collection_data:
        if field in update_data:
            setattr(collection, field, update_data[field])

    db_session.commit()
    return collection


def delete(db_session: Session, collection: Collection) -> None:
    db_session.delete(collection)
    db_session.commit()
