from typing import Optional

from pydantic import BaseModel, ConfigDict


class MessageSend(BaseModel):
    queue: str
    exchange: str
    data: str


class MessageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    queue: Optional[str]
    exchange: Optional[str]
    body: Optional[str]


class MessageReadMinimal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
