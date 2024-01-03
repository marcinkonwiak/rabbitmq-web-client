from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database.core import Base
from src.models import ItemSettingsMixin


class Collection(Base, ItemSettingsMixin):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    messages = relationship("Message", back_populates="collection")
