from fastapi import APIRouter

from src.message.views import router as message_router
from src.ui.views import router as ui_router

router = APIRouter()

router.include_router(ui_router)
router.include_router(message_router, prefix="/message")
