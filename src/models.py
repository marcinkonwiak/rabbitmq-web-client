from pydantic import conint
from sqlalchemy import Column, String, Boolean, Integer

from database.core import Base

PrimaryKey = conint(gt=0, lt=2147483647)


class SettingsMixin(object):
    amqp_url = Column(String)
    queue = Column(String)
    exchange = Column(String)


class ItemSettingsMixin(SettingsMixin):
    inherit_settings = Column(Boolean, default=True, nullable=False)


class GlobalSettings(Base, SettingsMixin):
    __tablename__ = 'global_settings'

    id = Column(Integer, primary_key=True)
