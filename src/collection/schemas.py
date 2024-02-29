from collections.abc import Sequence
from dataclasses import dataclass
from typing import ClassVar

from fastapi import Form
from pydantic import BaseModel, ConfigDict

from src.message.schemas import MessageReadMinimal
from src.schemas import SettingsFormMixin, SettingsReadMixin
from src.ui.schemas import SidebarItem


class CollectionRead(BaseModel, SettingsReadMixin):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class CollectionReadMinimal(SidebarItem):
    model_config = ConfigDict(from_attributes=True)

    type: ClassVar[str] = "collection"
    messages: list[MessageReadMinimal]


class CollectionList(BaseModel):
    collections: Sequence[CollectionReadMinimal]


@dataclass
class CollectionUpdate(SettingsFormMixin):
    name: str = Form()
    body: str | None = Form(default=None)


@dataclass
class CollectionMove:
    prev_item_weight: float | None = Form(default=None)
