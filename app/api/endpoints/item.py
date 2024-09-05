from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.core.sql_alchemy_connection import get_db
from app.db.crud.item import get_item, create_item
from app.schemas.item_schema import ItemCreate, ItemResponse

item_router = APIRouter()

@item_router.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@item_router.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        # Add item to the database
        new_item = create_item(db, item)
        return new_item
    except Exception as e:
        # Log the exception (in a real application, you might use a logger here)
        print(f"An error occurred: {e}")
        # Raise a HTTP 500 error with a generic message
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred.")
