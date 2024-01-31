from abc import ABC
from typing import ClassVar

from pydantic import BaseModel


class SidebarItem(BaseModel, ABC):
    id: int
    name: str
    weight: float
    type: ClassVar[str]
