from database.core import DbSession
from fastapi import APIRouter, Request
from message.flows import get_message_data
from models import PrimaryKey
from templates import Templates

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
        "message/message.html", {"request": request, "message": message}
    )


@router.post("")
def send_message(
    request: Request,
    templates: Templates,
):
    return templates.TemplateResponse(
        "common/send_button/send_button_success.html", {"request": request}
    )
