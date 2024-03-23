from fastapi import APIRouter, Request

from src.database.core import DbSession
from src.templates import Templates
from src.ui.flows import CommonUIData, get_sidebar_items

router = APIRouter()


@router.get("/")
def index(ui_data: CommonUIData, request: Request, templates: Templates):
    return templates.HtmxAwareTemplateResponse(
        "dashboard/dashboard.html",
        {
            "request": request,
            **ui_data,
        },
    )


@router.get("/sidebar")
def sidebar(db_session: DbSession, request: Request, templates: Templates):
    return templates.HtmxAwareTemplateResponse(
        "common/sidebar/sidebar.html",
        {
            "request": request,
            "sidebar_items": get_sidebar_items(db_session),
        },
    )
