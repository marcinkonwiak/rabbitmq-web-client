from collection import service as collection_service
from collection.schemas import CollectionList
from sqlalchemy.orm import Session


def get_collection_list(db_session: Session) -> CollectionList:
    return CollectionList(collections=collection_service.get_all(db_session))
