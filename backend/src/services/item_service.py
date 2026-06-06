from ..db.database import InMemoryDB
from ..models.item import Item, ItemCreate, ItemUpdate


class ItemService:
    def __init__(self, db: InMemoryDB):
        self.db = db

    def list_items(self) -> list[Item]:
        return list(self.db.items)

    def get_item(self, item_id: int) -> Item | None:
        return next((i for i in self.db.items if i.id == item_id), None)

    def create_item(self, payload: ItemCreate) -> Item:
        new_id = max((item.id for item in self.db.items), default=0) + 1
        item = Item(id=new_id, **payload.model_dump())
        self.db.items.append(item)
        return item

    def update_item(self, item_id: int, payload: ItemUpdate) -> Item | None:
        item = self.get_item(item_id)
        if item is None:
            return None

        updated_item = Item(id=item_id, **payload.model_dump())
        index = self.db.items.index(item)
        self.db.items[index] = updated_item
        return updated_item

    def delete_item(self, item_id: int) -> bool:
        item = self.get_item(item_id)
        if item is None:
            return False

        self.db.items.remove(item)
        return True
