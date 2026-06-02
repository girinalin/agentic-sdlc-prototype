from services.item_service import ItemService
from db.database import InMemoryDB

db = InMemoryDB()
service = ItemService(db)

def get_item_service():
    return service
