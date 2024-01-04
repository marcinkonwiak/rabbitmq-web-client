from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status

from src.database.core import DbSession
from src.models import PrimaryKey
from src.templates import Templates

from .flows import get_message_data
from .schemas import MessageUpdate
from .service import get, update

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
    message_id: PrimaryKey,
    message_in: Annotated[MessageUpdate, Depends()],
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    message = get(db_session, message_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A message with this id does not exist."}],
        )

    update(db_session, message, message_in)

    return templates.TemplateResponse(
        "common/send_button/send_button_success.html", {"request": request}
    )
