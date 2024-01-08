from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .models import Message
from .schemas import MessageRead
from .service import get


def get_message_from_id(db_session: Session, message_id: int) -> Message:
    if not (message := get(db_session, message_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A message with this id does not exist."}],
        )

    return message


def get_message_data(message: Message) -> MessageRead:
    return MessageRead.model_validate(message)
