from services.item_service import ItemService
from db.database import InMemoryDB
from models.item import ItemCreate

def test_create_item():
    db = InMemoryDB()
    service = ItemService(db)

    item = service.create_item(ItemCreate(name="Test", description="Demo"))
    assert item.id == 1
    assert item.name == "Test"

def test_list_items():
    db = InMemoryDB()
    service = ItemService(db)

    service.create_item(ItemCreate(name="A"))
    service.create_item(ItemCreate(name="B"))

    items = service.list_items()
    assert len(items) == 2

def test_update_item_success():
    db = InMemoryDB()
    service = ItemService(db)
    item_data = {"name": "Updated Item"}
    result = service.update_item("123", item_data)
    assert result["name"] == "Updated Item"
