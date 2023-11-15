from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from collection.models import Collection


def get(db_session: Session, collection_id: int) -> Optional[Collection]:
    return db_session.get(Collection, collection_id)


def get_all(db_session: Session) -> Sequence[Collection]:
    return db_session.execute(select(Collection)).scalars().all()
