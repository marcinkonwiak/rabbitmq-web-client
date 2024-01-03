from sqlalchemy.orm import Session

from src.collection import service as collection_service

from .schemas import CollectionList


def get_collection_list(db_session: Session) -> CollectionList:
    return CollectionList(collections=collection_service.get_all(db_session))
