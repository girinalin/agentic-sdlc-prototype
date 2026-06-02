from fastapi import APIRouter, HTTPException, Depends
from models.item import Item, ItemCreate
from services.item_service import ItemService
from api.dependencies import get_item_service

router = APIRouter()

@router.get("/items", response_model=list[Item])
def list_items(service: ItemService = Depends(get_item_service)):
    return service.list_items()

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate, service: ItemService = Depends(get_item_service)):
    return service.create_item(payload)

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, service: ItemService = Depends(get_item_service)):
    service.delete_item(item_id)
