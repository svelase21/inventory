from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Supplier(Base):
    __tablename__ = "supplier"

    code = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationship with Order
    order = relationship("Order", back_populates="order_supplier")