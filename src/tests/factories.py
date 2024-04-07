from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText

from src.message.models import Message

from .conftest import TestSessionLocal


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = TestSessionLocal()
        sqlalchemy_session_persistence = "commit"


class MessageFactory(BaseFactory):
    name = Sequence(lambda n: f"Message {n}")
    body = FuzzyText()
    weight = FuzzyInteger(0, 100)

    class Meta:
        model = Message
