from dataclasses import dataclass

from fastapi import Form
from pydantic import BaseModel, ConfigDict

from src.schemas import SettingsFormMixin, SettingsReadMixin


class MessageRead(BaseModel, SettingsReadMixin):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    body: str | None


class MessageReadMinimal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


@dataclass
class MessageUpdate(SettingsFormMixin):
    name: str = Form()
    body: str | None = Form(default=None)
