from typing import Annotated

from fastapi import APIRouter, Depends, Request

from src.database.core import DbSession
from src.models import PrimaryKey
from src.templates import Templates

from .flows import get_message_data
from .schemas import MessageSend

router = APIRouter()


@router.get("/{message_id}")
def get_message(
    message_id: PrimaryKey,
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    message = get_message_data(db_session, message_id)

    return templates.HtmxAwareTemplateResponse(
        "message/message.html",
        {
            "request": request,
            "message": message,
        },
    )


@router.post("/{message_id}")
def send_message(
    message: Annotated[MessageSend, Depends()],
    request: Request,
    templates: Templates,
):
    return templates.TemplateResponse(
        "common/send_button/send_button_success.html", {"request": request}
    )
