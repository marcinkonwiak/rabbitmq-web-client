from message.schemas import MessageReadMinimal
from pydantic import BaseModel, ConfigDict


class CollectionReadMinimal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    messages: list[MessageReadMinimal]


class CollectionList(BaseModel):
    collections: list[CollectionReadMinimal]
