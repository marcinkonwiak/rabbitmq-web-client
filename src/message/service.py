from dataclasses import asdict

from sqlalchemy.orm import Session

from .models import Message
from .schemas import MessageUpdate


def get(db_session: Session, message_id: int) -> Message | None:
    return db_session.get(Message, message_id)


def update(
    db_session: Session,
    message: Message,
    message_in: MessageUpdate,
) -> Message:
    message_data = message.dict()
    update_data = asdict(message_in)

    for field in message_data:
        if field in update_data:
            setattr(message, field, update_data[field])

    db_session.commit()
    return message
