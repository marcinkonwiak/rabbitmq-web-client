from typing import List

from pydantic import BaseModel, ConfigDict

from message.schemas import MessageReadMinimal


class CollectionReadMinimal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    messages: List[MessageReadMinimal]


class CollectionList(BaseModel):
    collections: List[CollectionReadMinimal]
