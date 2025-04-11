from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.OrderOut)
def create(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@router.get("/{order_id}", response_model=schemas.OrderOut)
def read(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/", response_model=list[schemas.OrderOut])
def list_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.list_orders(db, skip, limit)

@router.put("/{order_id}", response_model=schemas.OrderOut)
def update(order_id: int, status: schemas.OrderUpdateStatus, db: Session = Depends(get_db)):
    order = crud.update_order_status(db, order_id, status.status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order