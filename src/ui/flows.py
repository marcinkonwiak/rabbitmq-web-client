from typing import Annotated

from fastapi import Depends

from collection.flows import get_collection_list
from database.core import DbSession


def get_common_ui_data(db_session: DbSession) -> dict:
    return {"collections": get_collection_list(db_session).collections}


CommonUIData = Annotated[dict, Depends(get_common_ui_data)]
