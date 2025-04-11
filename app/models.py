from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base
import enum

class OrderStatus(str, enum.Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"  # ✅ Corrected line
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
