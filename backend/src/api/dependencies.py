from ..db.database import InMemoryDB
from ..services.item_service import ItemService

db = InMemoryDB()
service = ItemService(db)


def get_item_service():
    return service
