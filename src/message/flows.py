from database.core import DbSession
from message import service as message_service
from message.schemas import MessageRead


def get_message_data(db_session: DbSession, message_id: int) -> MessageRead:
    return MessageRead.model_validate(message_service.get(db_session, message_id))
