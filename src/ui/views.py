from fastapi import APIRouter, Request

from src.collection.flows import get_collection_list
from src.database.core import DbSession
from src.templates import Templates

router = APIRouter()


@router.get("/")
def index(request: Request, db_session: DbSession, templates: Templates):
    collection_list = get_collection_list(db_session)

    return templates.HtmxAwareTemplateResponse(
        "dashboard/dashboard.html",
        {"request": request, "collections": collection_list.collections},
    )
