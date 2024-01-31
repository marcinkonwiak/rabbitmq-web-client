from typing import Annotated

from fastapi import Depends

from src.database.core import DbSession
from src.ui.schemas import SidebarItem


def get_common_ui_data(db_session: DbSession) -> dict:
    return {
        "sidebar_items": get_sidebar_items(db_session),
    }


CommonUIData = Annotated[dict, Depends(get_common_ui_data)]


def get_sidebar_items(db_session: DbSession) -> list[SidebarItem]:
    from src.collection.flows import get_collection_list
    from src.message.flows import get_messages_without_parent

    collections = get_collection_list(db_session).collections
    messages = get_messages_without_parent(db_session).messages

    sidebar_items: list[SidebarItem] = []
    sidebar_items.extend(messages)
    sidebar_items.extend(collections)

    sidebar_items.sort(key=lambda i: i.weight)

    return sidebar_items


def move_sidebar_item(
    item: SidebarItem,
    next_item_weight: float | None,
    prev_item_weight: float | None,
) -> SidebarItem:
    if prev_item_weight is None:
        prev_item_weight = 0

    if next_item_weight:
        item.weight = (prev_item_weight + next_item_weight) / 2
    else:
        item.weight = prev_item_weight + 1

    return item
