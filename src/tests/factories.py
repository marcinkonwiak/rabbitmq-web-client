from factory import Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText

from src.collection.models import Collection
from src.message.models import Message

from .conftest import db_session


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db_session
        sqlalchemy_session_persistence = "commit"


class CollectionFactory(BaseFactory):
    name = Sequence(lambda n: f"Collection {n}")
    weight = FuzzyInteger(0, 100)

    class Meta:
        model = Collection


class MessageFactory(BaseFactory):
    name = Sequence(lambda n: f"Message {n}")
    body = FuzzyText()
    weight = FuzzyInteger(0, 100)
    collection = SubFactory(CollectionFactory)

    class Meta:
        model = Message
