from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from src.database.core import Base
from src.models import ItemSettingsMixin


class Collection(Base, ItemSettingsMixin):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False, default=0)

    messages = relationship(
        "Message", back_populates="collection", cascade="all, delete"
    )
