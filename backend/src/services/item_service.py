from models.item import Item, ItemCreate
from db.database import InMemoryDB

class ItemService:
    def __init__(self, db: InMemoryDB):
        self.db = db

    def list_items(self):
        return self.db.items

    def get_item(self, item_id: int):
        return next((i for i in self.db.items if i.id == item_id), None)

    def create_item(self, payload: ItemCreate):
        new_id = len(self.db.items) + 1
        item = Item(id=new_id, **payload.dict())
        self.db.items.append(item)
        return item

    def delete_item(self, item_id: int):
        self.db.items = [i for i in self.db.items if i.id != item_id]
