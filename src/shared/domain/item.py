from fastapi import APIRouter
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str

router = APIRouter()

@router.post("/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "id": item.id, "name": item.name}

@router.get("/id/{id}")
async def get_item(id: int):
    return {"message": "Item Found", "id": id, "name": "Test Item"}