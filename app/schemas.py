from pydantic import BaseModel
from typing import Optional
from enum import Enum

class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class OrderBase(BaseModel):
    customer_name: str
    item_name: str
    quantity: int
    price: float

class OrderCreate(OrderBase):
    pass

class OrderUpdateStatus(BaseModel):
    status: OrderStatus

class OrderOut(OrderBase):
    id: int
    status: OrderStatus

    class Config:
        orm_mode = True