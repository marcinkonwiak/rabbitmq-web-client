from pydantic import BaseModel, ConfigDict

from src.schemas import SettingsReadMixin


class MessageSend(BaseModel):
    routing_key: str
    exchange: str
    data: str


class MessageRead(BaseModel, SettingsReadMixin):
    model_config = ConfigDict(from_attributes=True)

    name: str
    body: str | None


class MessageReadMinimal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
