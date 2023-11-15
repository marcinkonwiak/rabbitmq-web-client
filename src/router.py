from fastapi import APIRouter

from ui.views import router as ui_router
from message.views import router as message_router

router = APIRouter()

router.include_router(ui_router)
router.include_router(message_router, prefix="/message")
