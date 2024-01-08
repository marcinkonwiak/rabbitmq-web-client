from dataclasses import asdict

from sqlalchemy.orm import Session

from .models import Message
from .schemas import MessageUpdate


def get(db_session: Session, message_id: int) -> Message | None:
    return db_session.get(Message, message_id)


def create(db_session: Session) -> Message:
    message = Message(name="New Message")
    db_session.add(message)
    db_session.commit()

    return message


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


def delete(db_session: Session, message: Message) -> None:
    db_session.delete(message)
    db_session.commit()
