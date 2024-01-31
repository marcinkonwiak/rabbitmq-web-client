from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Message


def get(db_session: Session, message_id: int) -> Message | None:
    return db_session.get(Message, message_id)


def create(db_session: Session, commit: bool = True) -> Message:
    message = Message(name="New Message")
    db_session.add(message)
    if commit:
        db_session.commit()

    return message


def update(
    db_session: Session,
    message: Message,
    update_data: dict,
) -> Message:
    message_data = message.dict()

    for field in message_data:
        if field in update_data:
            setattr(message, field, update_data[field])

    db_session.commit()
    return message


def delete(db_session: Session, message: Message) -> None:
    db_session.delete(message)
    db_session.commit()


def get_without_parents(db_session: Session) -> Sequence[Message]:
    return (
        db_session.execute(select(Message).where(Message.collection_id.is_(None)))
        .scalars()
        .all()
    )
