from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response

from src.database.core import DbSession
from src.models import PrimaryKey
from src.templates import Templates

from .flows import create_message as create_message_flow
from .flows import get_message_data, get_message_from_id, move, publish_message
from .schemas import MessageMove, MessageUpdate
from .service import delete, update

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
    message = create_message_flow(db_session)
    message_data = get_message_data(message)

    return templates.HtmxAwareTemplateResponse(
        "message/message.html",
        {
            "request": request,
            "message": message_data,
        },
        headers={
            "HX-Push-Url": f"/message/{message.id}",
            "HX-Trigger": "update-sidebar",
        },
    )


@router.post("/{message_id}")
def send_message(
    message_id: PrimaryKey,
    message_in: Annotated[MessageUpdate, Depends()],
    db_session: DbSession,
):
    message = get_message_from_id(db_session, message_id)
    headers = (
        {"HX-Trigger": "update-sidebar"} if message.name != message_in.name else {}
    )
    message = update(db_session, message, asdict(message_in))
    publish_message(message)

    return Response(
        status_code=204,
        headers=headers,
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
        headers={
            "HX-Replace-Url": "/",
            "HX-Trigger": "update-sidebar",
        },
    )


@router.post("/{message_id}/move")
def move_message(
    message_id: PrimaryKey,
    move_in: Annotated[MessageMove, Depends()],
    db_session: DbSession,
):
    message = get_message_from_id(db_session, message_id)
    move(db_session, message, move_in.collection_id, move_in.prev_item_weight)

    return Response(
        status_code=204,
        headers={"HX-Trigger": "update-sidebar"},
    )
