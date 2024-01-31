from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.ui.flows import move_sidebar_item
from src.ui.service import get_next_item_weight

from .models import Message
from .schemas import MessageList, MessageRead
from .service import create, get, get_without_parents


def get_message_from_id(db_session: Session, message_id: int) -> Message:
    if not (message := get(db_session, message_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A message with this id does not exist."}],
        )

    return message


def get_message_data(message: Message) -> MessageRead:
    return MessageRead.model_validate(message)


def get_messages_without_parent(db_session: Session) -> MessageList:
    messages = get_without_parents(db_session)

    return MessageList(messages=messages)


def create_message(db_session: Session) -> Message:
    message = create(db_session, False)
    next_item = get_next_item_weight(
        db_session,
        None,
        0,
        exclude_id=message.id,
    )
    move_sidebar_item(message, next_item, 0)
    db_session.commit()

    return message


def move(
    db_session: Session,
    message: Message,
    collection_id: str | None,
    prev_item_weight: float | None,
):
    next_item = get_next_item_weight(
        db_session,
        collection_id,
        prev_item_weight,
        exclude_id=message.id,
    )
    move_sidebar_item(message, next_item, prev_item_weight)

    message.collection_id = collection_id
    db_session.commit()
