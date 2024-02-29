from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response

from src.database.core import DbSession
from src.models import PrimaryKey
from src.templates import Templates

from .flows import get_collection_data, get_collection_from_id, move
from .schemas import CollectionMove, CollectionUpdate
from .service import delete, update

router = APIRouter()


@router.get("/{collection_id}")
def get_collection(
    collection_id: PrimaryKey,
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    collection = get_collection_from_id(db_session, collection_id)
    collection_data = get_collection_data(collection)

    return templates.HtmxAwareTemplateResponse(
        "collection/collection.html",
        {
            "request": request,
            "collection": collection_data,
        },
    )


@router.post("/{collection_id}")
def update_collection(
    collection_id: PrimaryKey,
    collection_in: Annotated[CollectionUpdate, Depends()],
    db_session: DbSession,
):
    collection = get_collection_from_id(db_session, collection_id)
    headers = (
        {"HX-Trigger": "update-sidebar"}
        if collection.name != collection_in.name
        else {}
    )
    update(db_session, collection, asdict(collection_in))

    return Response(
        status_code=204,
        headers=headers,
    )


@router.delete("/{collection_id}")
def delete_collection(
    collection_id: PrimaryKey,
    request: Request,
    db_session: DbSession,
    templates: Templates,
):
    collection = get_collection_from_id(db_session, collection_id)
    delete(db_session, collection)

    return templates.TemplateResponse(
        "dashboard/dashboard.html",
        {"request": request},
        headers={
            "HX-Replace-Url": "/",
            "HX-Trigger": "update-sidebar",
        },
    )


@router.post("/{collection_id}/move")
def move_collection(
    collection_id: PrimaryKey,
    move_in: Annotated[CollectionMove, Depends()],
    db_session: DbSession,
):
    collection = get_collection_from_id(db_session, collection_id)
    move(db_session, collection, move_in.prev_item_weight)

    return Response(
        status_code=204,
        headers={"HX-Trigger": "update-sidebar"},
    )
