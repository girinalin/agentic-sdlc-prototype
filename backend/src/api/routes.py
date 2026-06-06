from fastapi import APIRouter, HTTPException, Depends

from ..models.item import Item, ItemCreate, ItemUpdate
from ..services.item_service import ItemService
from .dependencies import get_item_service

router = APIRouter()


@router.get("/items", response_model=list[Item])
def list_items(service: ItemService = Depends(get_item_service)):
    return service.list_items()


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item = service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate, service: ItemService = Depends(get_item_service)):
    return service.create_item(payload)


@router.put("/items/{item_id}", response_model=Item)
def update_item(
    item_id: int,
    payload: ItemUpdate,
    service: ItemService = Depends(get_item_service),
):
    item = service.update_item(item_id, payload)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, service: ItemService = Depends(get_item_service)):
    if not service.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
