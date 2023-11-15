from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.core import Base
from models import ItemSettingsMixin


class Message(Base, ItemSettingsMixin):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    body = Column(String)

    collection_id = Column(Integer, ForeignKey("collection.id"))
    collection = relationship("Collection", back_populates="messages")
