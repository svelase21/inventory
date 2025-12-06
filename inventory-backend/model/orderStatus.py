from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class OrderStatus(Base):
    __tablename__ = "order_status"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)

    # Relationship with Order
    order = relationship("Order", back_populates="order_status")
