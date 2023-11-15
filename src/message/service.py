from typing import Optional

from sqlalchemy.orm import Session

from message.models import Message


def get(db_session: Session, message_id: int) -> Optional[Message]:
    return db_session.get(Message, message_id)
