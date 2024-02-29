from collections.abc import Sequence
from dataclasses import dataclass
from typing import ClassVar

from fastapi import Form
from pydantic import BaseModel, ConfigDict

from src.schemas import SettingsFormMixin, SettingsReadMixin
from src.ui.schemas import SidebarItem


class MessageRead(BaseModel, SettingsReadMixin):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    body: str | None


class MessageReadMinimal(SidebarItem):
    model_config = ConfigDict(from_attributes=True)
    type: ClassVar[str] = "message"


class MessageList(BaseModel):
    messages: Sequence[MessageReadMinimal]


@dataclass
class MessageUpdate(SettingsFormMixin):
    name: str = Form()
    body: str | None = Form(default=None)


@dataclass
class MessageMove:
    collection_id: int | None = Form(default=None)
    prev_item_weight: float | None = Form(default=None)
