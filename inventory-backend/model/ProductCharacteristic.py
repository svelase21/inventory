from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class ProductCharacteristic(Base):
    __tablename__ = "product_characteristic"

    # --- Start - relations many to one ---
    product_code = Column(Integer, ForeignKey("product.code"), primary_key=True, nullable=False)
    characteristic_id = Column(Integer, ForeignKey("characteristic.id"), primary_key=True, nullable=False)
    # --- End - relations many to one ---

    # --- Start Back populates - connect with entities ---
    product = relationship("Product", back_populates="characteristics")
    characteristic = relationship("Characteristic", back_populates="products")
    # --- End Back populates - connect with entities ---