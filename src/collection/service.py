from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Collection


def get(db_session: Session, collection_id: int) -> Collection | None:
    return db_session.get(Collection, collection_id)


def get_all(db_session: Session) -> Sequence[Collection]:
    return db_session.execute(select(Collection)).scalars().all()
