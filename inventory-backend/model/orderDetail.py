from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class OrderDetail(Base):
    __tablename__ = "order_detail"

    # --- Start - relations many to one ---
    order_code = Column(Integer, ForeignKey("order.code"), primary_key=True, nullable=False)
    product_code = Column(Integer, ForeignKey("product.code"), primary_key=True, nullable=False)
    # --- End - relations many to one ---
    amount = Column(Integer)

    # --- Start Back populates - connect with entities ---
    order = relationship("Order", back_populates="products")
    product = relationship("Product", back_populates="orders")
    # --- End Back populates - connect with entities ---