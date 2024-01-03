from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.core import Base
from src.models import ItemSettingsMixin


class Message(Base, ItemSettingsMixin):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    body = Column(String)

    collection_id = Column(Integer, ForeignKey("collection.id"))
    collection = relationship("Collection", back_populates="messages")
