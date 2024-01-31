from typing import Annotated

from fastapi import APIRouter, Depends, Response

from src.database.core import DbSession
from src.models import PrimaryKey

from .flows import get_collection_from_id, move
from .schemas import CollectionMove

router = APIRouter()


@router.post("/{collection_id}/move")
def move_message(
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
