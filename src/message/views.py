from typing import Annotated

from fastapi import APIRouter, Depends, Request

from src.database.core import DbSession
from src.models import PrimaryKey
from src.templates import Templates

from .flows import get_message_data, get_message_from_id
from .schemas import MessageUpdate
from .service import create, delete, update

router = APIRouter()


@router.get("/{message_id}")
def get_message(
    message_id: PrimaryKey,
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    message = get_message_from_id(db_session, message_id)
    message_data = get_message_data(message)

    return templates.HtmxAwareTemplateResponse(
        "message/message.html",
        {
            "request": request,
            "message": message_data,
        },
    )


@router.post("/")
def create_message(
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    message = create(db_session)
    message_data = get_message_data(message)

    return templates.HtmxAwareTemplateResponse(
        "message/message.html",
        {
            "request": request,
            "message": message_data,
        },
        headers={"HX-Push-Url": f"/message/{message.id}"},
    )


@router.post("/{message_id}")
def send_message(
    message_id: PrimaryKey,
    message_in: Annotated[MessageUpdate, Depends()],
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    message = get_message_from_id(db_session, message_id)
    update(db_session, message, message_in)

    return templates.TemplateResponse(
        "common/send_button/send_button_success.html",
        {"request": request},
    )


@router.delete("/{message_id}")
def delete_message(
    message_id: PrimaryKey,
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    message = get_message_from_id(db_session, message_id)
    delete(db_session, message)

    return templates.TemplateResponse(
        "dashboard/dashboard.html",
        {"request": request},
        headers={"HX-Replace-Url": "/"},
    )
