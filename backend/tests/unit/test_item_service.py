from backend.src.db.database import InMemoryDB
from backend.src.models.item import ItemCreate, ItemUpdate
from backend.src.services.item_service import ItemService


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
    item = service.create_item(ItemCreate(name="Original"))

    result = service.update_item(item.id, ItemUpdate(name="Updated Item"))

    assert result is not None
    assert result.name == "Updated Item"


def test_update_item_not_found():
    service = ItemService(InMemoryDB())

    result = service.update_item(999, ItemUpdate(name="Missing"))

    assert result is None


def test_delete_item():
    service = ItemService(InMemoryDB())
    item = service.create_item(ItemCreate(name="Delete me"))

    assert service.delete_item(item.id) is True
    assert service.get_item(item.id) is None
    assert service.delete_item(item.id) is False
