from sqlalchemy.orm import Session
from app.db.models.item import Item
from app.schemas.item_schema import ItemCreate


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # Get the updated instance with the ID
    return db_item