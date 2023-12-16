from database.core import Base
from models import ItemSettingsMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Collection(Base, ItemSettingsMixin):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    messages = relationship("Message", back_populates="collection")
