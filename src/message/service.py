from message.models import Message
from sqlalchemy.orm import Session


def get(db_session: Session, message_id: int) -> Message | None:
    return db_session.get(Message, message_id)
