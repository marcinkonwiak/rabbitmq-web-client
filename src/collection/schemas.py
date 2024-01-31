from collections.abc import Sequence
from dataclasses import dataclass
from typing import ClassVar

from fastapi import Form
from pydantic import BaseModel, ConfigDict

from src.message.schemas import MessageReadMinimal
from src.ui.schemas import SidebarItem


class CollectionReadMinimal(SidebarItem):
    model_config = ConfigDict(from_attributes=True)

    type: ClassVar[str] = "collection"
    messages: list[MessageReadMinimal]


class CollectionList(BaseModel):
    collections: Sequence[CollectionReadMinimal]


@dataclass
class CollectionMove:
    prev_item_weight: float | None = Form(default=None)
