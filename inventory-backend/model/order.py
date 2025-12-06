from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "order"

    code = Column(Integer, primary_key=True, index=True)

    # Relationship many to one
    status = Column(Integer, ForeignKey("order_status.id"))
    supplier = Column(Integer, ForeignKey("supplier.code"))
    order_date = Column(DateTime, nullable=False)
    ship_date = Column(DateTime, nullable=False)

    # Relationship with OrderStatus
    order_status = relationship("OrderStatus", back_populates="order")

    # Relationship with Supplier
    order_supplier = relationship("Supplier", back_populates="order")

    # Relationship with OrderDetail
    products = relationship("OrderDetail", back_populates="order")