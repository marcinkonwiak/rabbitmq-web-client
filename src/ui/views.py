from fastapi import APIRouter, Request

from collection.flows import get_collection_list
from database.core import DbSession
from templates import Templates


router = APIRouter()


@router.get("/")
def index(request: Request, db_session: DbSession, templates: Templates):
    collection_list = get_collection_list(db_session)

    return templates.TemplateResponse(
        "dashboard/dashboard.html",
        {"request": request, "collections": collection_list.collections},
    )
